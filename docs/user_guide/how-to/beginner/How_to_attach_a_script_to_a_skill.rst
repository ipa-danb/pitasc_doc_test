=================================
How to attach a script to a skill
=================================

The way to attach scripts to skills is almost the same as attaching a monitor. First you have to include the script
by adding the include statement at the start of the ``<models>`` tag.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="package_name" file="path/script_file.xml"/>
        ...

.. Comment to get indent after code-block
..

.. note::
    | For adding all in pitasc already defined scripts, use the following include statement, which you can also find in every example application file.
    | ``<include package="pitasc_library" file="models/pitasc.xml"/>``

There are two options for attaching a script to a skill. The first option is to create a child of the script
directly inside the ``<member id="scripts">`` tag of the skill. You can either use the ``<clone>`` or the ``<type>``
tag to add a script. For more information about these tags and there use look at
:doc:`../advanced/How_to_add_a_parameter_to_a_skill_monitor_etc`.

.. code-block:: xml
    :emphasize-lines: 2,3,4,5

    <member id="scripts">
        <clone id="script_id" prototype="script_example">
            <member id="parameter">value</member>
            ...
        </clone>
    </member>

The second option is to create the child of the script outside the ``<member id="scripts">`` tag
as a parameter of the skill and create a reference to this script parameter using the ``<reference>`` tag inside
the ``<member id="scripts">`` tag. This option has lower readability and thus, it is not recommended.

.. note::
    See also the xml reference of :doc:`../../../xml_reference/scripts/index`

**Example 1: Attach script to skill**

.. code-block:: xml
    :emphasize-lines: 18, 19, 20, 21, 22

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
                            <member id="scripts">
                                <!-- calls my ros service at the beginning of the skill without blocking -->
                                <clone prototype="script_call_trigger_srvs">
                                    <member id="service_name">/my_service</member>
                                    <member id="blocking">False</member>
                                    <member id="on_start">True</member>
                                </clone>
                            </member>
                        </clone>
                    </member>
                </clone>
            </member>
        </clone>
    </pitasc>



**Example 2: Attach script to skill definition**

.. code-block:: xml
    :emphasize-lines: 7, 8, 9

    <type id="skill_call_my_service" prototype="skill_idle_once">
        <meta>
            <member id="description">Calls my special std_srvs/Trigger service</member>
        </meta>
        <data>
            <member id="scripts">
                <clone prototype="script_call_trigger_srvs">
                    <member id="service_name">/my_service</member>
                </clone>
            </member>
        </data>
    </type>

.. note::
    
    In this example, a ``skill_idle_once`` is used as prototype, which continues after one pitasc cycle. So, the ``blocking`` member of ``script_call_trigger_srvs`` must be ``false`` (which is the default value). Another (possibly better) way is to use a ``skill_idle`` as prototype and add also a ``monitor_script_result`` to handle the results of the trigger service respectively.
