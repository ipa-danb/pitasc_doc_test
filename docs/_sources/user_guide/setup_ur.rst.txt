==============
Setup UR Robot
==============


Requirements
============

UR e-series (recommended) or CB3


Install UR driver and setup
===========================

- Optional/Recommended: Follow the `Realtime Kernel setup guide <https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/ur_robot_driver/doc/real_time.md>`_
- `Install the ur driver <https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/README.md#install-from-binary-packages>`_

Setup the network connection
----------------------------

#.
   Open the network settings from the UR teach pendant (Setup Robot -> Network) and enter these settings (possibly adapt the ip space `192.168.1.xx` to your needs):

    .. code-block::

        IP address: 192.168.1.102
        Subnet mask: 255.255.255.0
        Default gateway: 192.168.1.1
        Preferred DNS server: 192.168.1.1
        Alternative DNS server: 0.0.0.0


#.
   On the remote PC, turn off all network devices except the "wired connection", e.g. turn off wifi.

#.
   Open Network Settings and create a new Wired connection with these settings. You may want to name this new connection ``UR`` or something similar:

    .. code-block::

        IPv4
        Manual
        Address: 192.168.1.101
        Netmask: 255.255.255.0
        Gateway: 192.168.1.1


#. Verify the connection from the PC with e.g. ping. ``192.168.1.102`` is the robot ip in this case.

    .. code-block:: console

        ping 192.168.1.102


Set up the robot
----------------

Follow the instructions of the ur robot driver: `Setup the robot <https://github.com/UniversalRobots/Universal_Robots_ROS_Driver/blob/master/README.md#setting-up-a-ur-robot-for-ur_robot_driver>`_
(Use the ip you set above)

Note:
You can download the calibration correction and use it in your package like this: 

.. code-block:: console

    roslaunch ur_calibration calibration_correction.launch robot_ip:=192.168.1.102 target_filename:="${HOME}/catkin_ws/src/<your_ros_package>/config/ur10e_kinematics.yaml"



ROS launch file
===============

We recommend putting the robot into a namespace, e.g. ``/robot``. The following launchfile loads the driver for a UR10e robot. Use the ip you set on the robot

.. code-block:: xml

    <?xml version="1.0"?>

    <launch>
        <arg name="robot_ip" default="192.168.1.102"/>
        <group ns="robot">

            <!-- ROS control: make pitasc controller available -->
            <rosparam command="load" file="$(find pitasc_controller)/controller/pitasc_controller.yaml"/>

            <!-- robot driver (official) -->
            <include file="$(find ur_robot_driver)/launch/ur10e_bringup.launch">
                <arg name="robot_ip" value="$(arg robot_ip)"/>
                <!-- create your own upload launch file for using your own robot description -->
                <!-- <arg name="robot_description_file" value="$(find <your_ros_package>)/launch/ur10e_upload.launch"/> -->
                <!-- enter the tf_prefix if you set it in a custom urdf -->
                <!-- <arg name="tf_prefix" value=""/> -->
                <arg name="controllers" default="joint_state_controller speed_scaling_state_controller force_torque_sensor_controller pitasc_vel_control"/>
                <arg name="stopped_controllers" default="joint_group_vel_controller"/>
                <!-- use the factory calibration of your robot for higher accuracy -->
                <!-- <arg name="kinematics_config" default="$(find <your_ros_package>)/config/ur10e_kinematics.yaml"/> -->
            </include>

        </group>

    </launch>


pitasc environment
==================

To let pitasc take joint states and urdf description from the robot namespace, it needs to be configured. Set the urdf prefix if you have one (``tf_prefix`` in the ur launch file)

.. code-block:: xml

    <pitasc>
        <models>
            (...)
            <include package="pitasc_library" file="universal_robots/ur.xml"/>
        </models>

        <clone prototype="project">

            <member id="configuration">
                <!-- Use the default configuration with 500Hz rate (for e series, 125Hz for CB3) -->
                <clone id="configuration" prototype="default_configuration">
                    <member id="update_rate">500</member>
                </clone>
            </member>

            <member id="environment">
                <clone prototype="robot_ur10">
                    <member id="robot_driver.max_velocity">2.0</member>
                    <member id="robot_driver.max_acceleration">3.0</member>
                    <member id="namespace">robot</member>
                    <member id="urdf_prefix"></member>
                </clone>
            </member>

            <member id="applications">
            (...)

