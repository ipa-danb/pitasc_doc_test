============
Applications
============

An application is nothing more than a skill, but part of the member ``applications`` of a pitasc project.

.. code-block:: xml

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
                <clone id="first_app" prototype="skill_sequence">
                    <!-- Your application -->
                </clone>
                <clone id="second_app" prototype="skill_lin">
                    <!-- Can be any skill type -->
                </clone>
                <!-- and so on.. -->
            </member>
        </clone>
    </pitasc>


.. note::
    See also :doc:`../how-to/beginner/How_to_create_an_application`

