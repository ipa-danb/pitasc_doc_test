====================================
How to add a skill to an application
====================================

To add a skill, you have to include the skill by adding the include statement at the start of the ``<models>`` tag.

.. rstcheck: ignore-next-code-block
.. code-block:: xml

    <pitasc>
        <models>
            <include package="package_name" file="path/skill_file.xml"/>
        ...

.. note::

    | For adding all in pitasc already defined skills, use the following include statement, which you can also find in every example application file.
    | ``<include package="pitasc_library" file="models/skills.xml"/>``


Add the skill inside the ``<member id="skills">`` tag of a composition skill (e.g., skill_sequence, skill_parallel).
You add the skill by creating a copy of the skill using the ``<clone>`` tag.

.. code-block:: xml
    :emphasize-lines: 3,9,10,11

    <pitasc>
        <models>
            <include package="your_package" file="skills/skill_[skill_file_name].xml"/> <!-- {parent_skill_id} -->
        </models>
        <clone prototype="project">
            <member id="applications">
                <clone id="my_app" prototype="skill_sequence">
                    <member id="skills">
                        <clone id="{skill_id}" prototype="{skill_type_name}">
                            <member id="{parameter}">{value}</member>
                            ...
                        </clone>
                    </member>
                </clone>
            </member>
        </clone>
    </pitasc>

.. Comment to get indent after code-block
..

    Replace ``{skill_id}`` by a locally unique name. If ``id`` is not set, the id is set to the prototype appended by a number if multiple skills
    of the same type are already existing at this point.

    Replace ``{skill_type_name}`` with the name of the skill you want to create

    Set skill parameters by using ``member`` tags and replacing ``{parameter}`` and ``{value}`` with the respective skill parameter name and the desired value.

.. note::
    See also the xml reference of :doc:`../../../xml_reference/skills/index`

**Example:**

.. code-block:: xml
    :emphasize-lines: 9, 32, 33, 34, 35, 36

    <?xml version="1.0" encoding="UTF-8"?>
    <pitasc>
        <models>
            <!-- Include pitasc -->
            <include package="pitasc_library" file="models/pitasc.xml"/>
            <!-- Include the UR5 -->
            <include package="pitasc_library" file="universal_robots/ur.xml"/>
            <!-- Include the skills -->
            <include package="pitasc_library" file="models/skills.xml"/>
        </models>

        <!-- Create a project -->
        <clone prototype="project">
            <member id="configuration">
                <!-- Use the default configuration with recommended settings -->
                <clone id="configuration" prototype="default_configuration"/>
            </member>

            <member id="environment">
                <!-- Add a UR5 -->
                <clone prototype="robot_ur5">
                    <member id="robot_driver.max_velocity">2.0</member>
                    <member id="robot_driver.max_acceleration">3.0</member>
                </clone>
            </member>

            <member id="applications">
                <clone id="my_app" prototype="skill_sequence">
                    <member id="robot" reference_id="environment.robot_ur5"/>
                    <member id="skills">
                        <!-- Move to starting position -->
                        <clone prototype="skill_lin">
                            <member id="tool_frame">tool</member>
                            <member id="target_frame">start_position</member>
                            <member id="target_offsets">0.0, -0.15, 0.0, 0.0, 0, 0.0</member>
                        </clone>
                    </member>
                </clone>
            </member>
        </clone>
    </pitasc>
