================
Setup KUKA Robot
================

Requirements
============

- Robot controller: KRC2, KRC4 or KRC5
- Option RSI3, RSI4 or RSI5.

Install driver and setup
===========================

Until the relative command patch is merged, use the fork `rsi4_with_velocity_interface <https://github.com/ipa-jsk/kuka_experimental/tree/rsi4_with_velocity_interface>`_ instead of the `main repository <https://github.com/ros-industrial/kuka_experimental>`_.

1. Optional/Recommended: Follow the `Realtime Kernel setup guide <https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/real_time.md>`_
2. Depending on your KRC version, follow one of the guides per the READMEs below to install the driver

   - `KRC2 <https://github.com/ipa-jsk/kuka_experimental/tree/rsi4_with_velocity_interface/kuka_rsi_hw_interface/krl/KR_C2>`_
   - `KRC4 <https://github.com/ipa-jsk/kuka_experimental/tree/rsi4_with_velocity_interface/kuka_rsi_hw_interface/krl/KR_C4>`_
   - `KRC5 <https://github.com/ipa-jsk/kuka_experimental/tree/rsi4_with_velocity_interface/kuka_rsi_hw_interface/krl/KR_C4>`_

Notes
-----

- Make sure that your ROS PC is connected to the right physical interface (ethernet port) on the KUKA controller. There are usually two interfaces of interest: one for transferring e.g. WorkVisual projects and the other for control with e.g. RSI.
- There is usually a detailed documentation of RSI (and the other installed options) on your controller; refer to that for more information (i.e. ways to debug). (E.g. Log in at least as an Expert on the Teach Pad, then navigate to :code:`KUKA_DATA D(:\\)\\KUKA_OPT\\RobotSensorInterface\\DOC`).

Optional
--------

Make a backup of current KRC configuration before driver installation. (See also: https://www.youtube.com/watch?v=PtVohrofnLY)

1. Insert USB stick to robot controller cabinet
2. Change user group level to "Expert"
3. In File navigator select :code:`Archiv:\\`
4. Select Archiv everything on USB(cabinet)

ROS launch file
===============

To start the communication with the KUKA controller a ROS launch file is required. The following ROS launch file loads the driver for a KUKA KR270 robot. We recommend putting the robot into a namespace, for this example we use the robot model: e.g. ``/KUKA-KR270``.
The lines of code which have to be changed for your robot are marked by in-line comments.


.. code-block:: xml

    <?xml version="1.0"?>

    <launch>
        <arg name="rsi_listen_address" doc="IP address of the PC running the ROS driver node" default="172.22.10.22" /> <-- Change to your IP -->
        <arg name="rsi_listen_port"    doc="Port number for the RSI communication"            default="59152" /> <-- Change to your port -->

        <group ns="KUKA-KR270"> <-- Change to your choosen namespace -->
            <!-- ROBOT DESCRIPTION -->
            <param name="robot_description" command="$(find xacro)/xacro '$(find kuka_kr270_support)/urdf/kr270r2700.xacro'" /> <-- Adapt for your robot type -->

            <!-- ROBOT DRIVER (official) -->
            <rosparam file="$(find kuka_kr270_support)/config/joint_names_kr270r2700.yaml" /> <-- Adapt for your robot type -->
            <param name="rsi/listen_address" value="$(arg rsi_listen_address)" />
            <param name="rsi/listen_port" value="$(arg rsi_listen_port)" />
            <node pkg="kuka_rsi_hw_interface" type="kuka_hardware_interface_node" name="rsi_driver"
                output="screen" />

            <!-- ROS CONTROL -->
            <!-- load pitasc controllers -->
            <rosparam command="load" file="$(find pitasc_controller)/controller/pitasc_controller.yaml"/>
            <!-- load joint_state_controller -->
            <rosparam>
                joint_state_controller:
                    type: joint_state_controller/JointStateController
                    publish_rate: 250  # RSI update rate
            </rosparam>
            <!-- spawn controllers -->
            <node name="controller_spawner" pkg="controller_manager" type="spawner" respawn="false"
                args="joint_state_controller pitasc_vel_control" />

            <!-- TF -->
            <!-- joint states to TF -->
            <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher" />

        </group>

    </launch>


pitasc environment
==================

To let pitasc take joint states and urdf description from the robot namespace, it needs to be configured. Set the urdf prefix if you have one (``tf_prefix`` in the launch file).
The only change required in the following code example is the namespace you choose in the ROS launch file.

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <pitasc>
        <models>
            <!-- Include pitasc -->
            <include package="pitasc_library" file="models/pitasc.xml"/>

            <!-- Include the kuka robot-->
            <include package="pitasc_library" file="kuka/robot_kuka.xml"/>

            <!-- Include the idle skill -->
            <include package="pitasc_library" file="models/skills.xml"/>
        </models>
        <clone prototype="project">
            <member id="configuration">
                <clone id="configuration" prototype="default_configuration">
                    <member id="update_rate">250.0</member>
                </clone>
            </member>
            <member id="environment">
                <clone prototype="robot_kuka">
                    <!-- Set the limits for the joint control signals -->
                    <member id="robot_driver.max_velocity">1.5</member>
                    <member id="robot_driver.max_acceleration">1.5</member>

                    <!-- adjust the namespace to correspond to the one set in the launchfile -->
                    <member id="namespace">KUKA-KR270</member>

                    <!-- define any prefixes you might have set in the robot description  -->
                    <member id="urdf_prefix"></member>
                </clone>
            </member>
            <member id="applications">
                <clone prototype="skill_sequence">
                    <member id="robot" reference_id="environment.robot_kuka"/>
                    <member id="skills">
                        <clone prototype="skill_relative_ptp">
                            <member id="relative_joint_state">0, 0, 0, 0, 0, 0</member>
                        </clone>
                    </member>
                </clone>
            </member>
        </clone>
    </pitasc>

To start the application:

1. Start launch file:

    .. code-block:: console

        roslaunch <your_package_name> <your_launc_file_name.launch>

2. Start pitasc executor

    .. code-block:: console

        pitasc_executor_rossrv

3. Start :code:`rqt`, start the piteacher and load your xml file to start the program

    .. code-block:: console

        rqt -s "Pi Teacher"

