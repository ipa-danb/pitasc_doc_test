===================================
How to set the value of a parameter
===================================

There are three ways of editing the value of a parameter.

1. Set value by adding it inside the ``<member>`` tag.

    .. code-block:: xml

        <clone prototype="skill_example">
            <member id="parameter_1">value</member>
        </clone>

2. Set a value by referring to another parameter. If used, the parameter is like a pointer and does not hold data itself.

    .. code-block:: xml

        <clone prototype="skill_example">
            <member id="parameter_1" reference_id="parameter_0"/>
        </clone>

3. Edit list or dictionary parameters: The new parameter (here ``monitor_duration``) is placed within the ``monitors`` member tags. Basically this is the same as the first option.

    .. code-block:: xml

        <member id="monitors">                                      <!-- list of monitors(parameters) -->
            <clone prototype="monitor_duration">                    <!-- example monitor(parameter) -->
            </clone>
        </member>

    .. note::

        Currently there is no way to delete values from lists. In this example, the new duration monitor is added to the list, not touching the possibly already existing entries (which could come from the prototype).
