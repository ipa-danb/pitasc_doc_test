==================================
How to attach a monitor to a Skill
==================================

First, you have to include the monitor by adding the include statement at the start of the ``<models>`` tag.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="package_name" file="path/monitor_file.xml"/>
        ...

.. Comment to get indent after code-block
..

.. note::
    | For adding all in pitasc already defined monitors, use the following include statement, which you can also find in every example application file.
    | ``<include package="pitasc_library" file="models/pitasc.xml"/>``

There are two options for attaching a monitor to a skill. The first option is to create a child of the monitor
directly inside the ``<member id="monitors">`` tag of the skill. Either use the ``<clone>`` or the
``<type>`` tag to add a monitor. For more information about these tags and their uses, look at
:doc:`../advanced/How_to_add_a_parameter_to_a_skill_monitor_etc`.

.. code-block:: xml
    :emphasize-lines: 2,3,4,5

    <member id="monitors">
        <clone id="monitor_id" prototype="monitor_example">
            <member id="parameter">value</member>
            ...
        </clone>
    </member>

The second option is to create the child of the monitor outside the ``<member id="monitors">`` tag
as a parameter of the skill and create a reference to this monitor parameter using the ``<reference>`` tag inside
the ``<member id="monitors">`` tag. This option has lower readability and thus, it is not recommended.

.. note::
    See also the xml reference of :doc:`../../../xml_reference/monitors/index`

**Example 1: Attach monitor to skill**

.. code-block:: xml
    :emphasize-lines: 17, 18, 19

    <pitasc>
        <...>

        <clone prototype="project">
            <...>

            <member id="applications">
                <clone prototype="skill_sequence">
                    <member id="robot" reference_id="environment.robot_ur5"/>
                    <member id="skills">
                        <!-- Move to starting position -->
                        <clone prototype="skill_lin">
                            <member id="tool_frame">tool</member>
                            <member id="target_frame">start_position</member>
                            <member id="target_offsets">0.0, -0.15, 0.0, 0.0, 0, 0.0</member>
                            <member id="monitors">
                                <!-- stops this skill after 3 seconds -->
                                <clone prototype="monitor_duration">
                                    <member id="duration">3</member>
                                </clone>
                            </member>
                        </clone>
                    </member>
                </clone>
            </member>
        </clone>
    </pitasc>

**Example 2: Attach monitor to skill definition**

.. code-block:: xml
    :emphasize-lines: 15, 16, 17, 18

    <type id="skill_idle_duration" prototype="skill_idle">
        <meta>
            <member id="description">A skill that keeps the robot position for a given duration</member>
        </meta>
        <data>
            <type id="duration" prototype="float_parameter">
                <meta>
                    <member id="description">Skill duration in [s].</member>
                    <member id="visibility">basic</member>
                </meta>
                <data>1.0</data>
            </type>

            <member id="monitors">
                <clone prototype="monitor_duration">
                    <member id="event">succeeded</member>
                    <member id="duration" reference_id="duration"/>
                </clone>
            </member>
        </data>
    </type>
