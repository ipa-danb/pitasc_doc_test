=========================================
How to access parameters inside cpp files
=========================================

To create C++ implementations for monitors or scripts, there are two functions to access the parameters defined in the ``.xml`` files.

The main way to access a parameter is the ``extract()`` function. It sets the value of the variable to the ``xml``
parameter value.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp

    extract(params["parameter_id"], variable);

Sometimes it is needed to cast the ``xml`` parameter value into another type before handing it to the variable.
This can be achieved with the ``extract_type()`` function.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp

    variable = extract_type(params["parameter_id"], type);

CVS (comma separated values) are a little bit more tricky. If only one value is inside the list and it is tried to put inside a vector, an error occurs. To avoid this, the statement can be placed inside a try and catch, that gives a waring if an error occurs. Subsequently, the value of the parameter is casted into the list type and added to a vector.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 2,7,8

    try {
        extract(params["parameter_id"], variables);
    } catch (std::invalid_argument&) {
        pi_warn("Parameter type of {} is not {}_csv. Automatic conversion from {}_parameter",
                "parameter_id", "type", "type");
        // coordinates is not a type_csv, but maybe a type_parameter, so lets try that instead
        auto variable = extract_type(params["parameter_id"], type);
        variables = vector<type>{variable};  // only single variable in this case
    }
