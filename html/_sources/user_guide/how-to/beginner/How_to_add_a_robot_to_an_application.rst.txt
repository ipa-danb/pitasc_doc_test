====================================
How to add a robot to an application
====================================

The robot can be included by adding the include statement at the start of the ``<models>`` tag. The ``.xml``
file to include the robot will usually be in a folder named 'robot_name' inside the package **pitasc_library**.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="pitasc_library" file="{robot_folder/robot_name}.xml"/>
        ...


As the second step, the robot should be added to the ``<member id="environment">`` tag of the project by cloning
the robot from the included ``.xml`` into it.

.. code-block:: xml
    :emphasize-lines: 2

    <member id="environment">
         <clone prototype="robot_id"/>
    </member>

As the last step, you need to set the ``robot`` parameter of the overarching composition skill inside the
``<member id="applications">`` to reference the robot added inside the ``<member id="environment">``

.. code-block:: xml
    :emphasize-lines: 3

    <member id="applications">
        <clone prototype="skill_sequence">
                <member id="robot" reference_id="environment.robot_id"/>
                ...
        </clone>
    </member>


| **Example**
| The complete pitasc application file should look something like the following example, in which a **UR5** robot
  is added.

.. code-block:: xml
    :emphasize-lines: 5,14,15,16,17,21
    :linenos:

    <pitasc>
        <models>
            <include package="pitasc_library" file="models/pitasc.xml"/>
            <include package="pitasc_library" file="models/skills.xml"/>
            <include package="pitasc_library" file="universal_robots/ur.xml"/>
        </models>

        <clone prototype="project">
            <member id="configuration">
                <!-- Use the default configuration with recommended settings -->
                <clone id="configuration" prototype="default_configuration"/>
            </member>

            <member id="environment">
                <!-- Add a UR5 -->
                <clone prototype="robot_ur5"/>
            </member>

            <member id="applications">
                <clone prototype="skill_sequence">
                    <member id="robot" reference_id="environment.robot_ur5"/>

                    <!-- skills -->

                </clone>
            </member>
        </clone>
    </pitasc>


| **Robot Parameters**
| Usually, you just need to set the namespace of the robot (if there is one) and the urdf prefix. 

But you can also explicitely define all parameters:

    .. code-block:: xml

        <pitasc>
            <...>

            <clone prototype="project">
                <...>

                <member id="environment">
                    <!-- Add a UR5 -->
                    <clone prototype="robot_ur5">
                        <member id="robot_driver.max_velocity">0.1</member>
                        <member id="robot_driver.max_acceleration">0.5</member>
                        <member id="robot_driver.topic_in">ur5/joint_states</member>
                        <member id="robot_driver.topic_out">ur5/joint_vel</member>
                        <member id="robot_driver.urdf_key">ur5/robot_description</member>
                        <member id="urdf_prefix"></member>
                        <member id="urdf_ee_link">ur5_tool0</member>
                        <member id="urdf_base_link">ur5_base_link</member>
                        <member id="namespace"></member>
                    </clone>
                </member>

                <...>
            </clone>
        </pitasc>
                   
Note that if you define a namespace, this is automatically added to the defined topics, following the ros namespace rules as it is in ros launch files. If you specify an urdf_prefix, this is added to the specified urdf_ee_link and urdf_base_link. 