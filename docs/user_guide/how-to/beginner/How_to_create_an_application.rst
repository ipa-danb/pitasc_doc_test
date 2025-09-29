============================
How to create an application
============================

The following code is the basis of every pitasc application file.

.. code-block:: xml
    :linenos:

    <pitasc>
        <models>
            <include package="pitasc_library" file="models/pitasc.xml"/>
            <include package="pitasc_library" file="models/skills.xml"/>
        </models>

        <clone prototype="project">
            <member id="configuration">
                <!-- Use the default configuration with recommended settings -->
                <clone id="configuration" prototype="default_configuration"/>
            </member>

            <member id="environment">
                <!-- robot and its components -->
            </member>

            <member id="applications">
                <clone prototype="skill_sequence">  <!-- composition skill -->
                    <!-- Your application -->
                </clone>
            </member>
        </clone>
    </pitasc>

The ``<pitasc>`` tag sets up the root node of the pitasc application file.

The ``<models>`` tag provides a place to include files containing skills, monitors, etc., The two
include files present in the code on top are the default include files and include everything that is part of
pitasc by default. They should be included in almost any application.

The ``<member id="configuration">`` tag includes every component needed to execute the application. This includes
the kinematic tree, the solver and the scene. The default configuration as seen in the code on top should be
sufficient and can be used in most cases.

Inside the ``<member id="environment">`` tag, the robot cell is modeled. This includes the robot and its
components like sensors and grippers.

The ``<member id="applications">`` tag is a list, in which the actual applications are placed. In addition
to the primary application, supporting applications like moving to the starting position are listed here. An
application is a skill or a composition skill e.g. **skill_sequence**, as shown in the code block above, that acts
as a container to hold multiple skills.

.. note::

    Later how to... tutorials will address these tags in more detail.

.. note::

    Check the example application files in ``pitasc_common/examples``.
