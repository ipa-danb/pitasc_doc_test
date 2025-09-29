=============================
How to use the operator class
=============================

Pitasc has a special operator parameter/class. In it, multiple comparison operators are implemented. This class is
mostly used by monitors. It allows us to change conditions of monitors simply by editing a parameter inside the
.xml, without needing to implement multiple operators inside the c++ ourselves. The following operations are
available.

.. code-block:: text

    greater              >
    greater_equal        >=
    equal                ==
    not_equal            !=
    less                 <
    less_equal           <=
    crossing_threshold

This guide explains how to use this operator class.

**xml**
=======

Add the parameter operator to your monitor/script by inheriting from the base operator class that only allows
viable values.

.. code-block:: xml

    <type id="operator" prototype="operator">
        <meta>
            <member id="visibility">required</member>
        </meta>
    </type>

**C++**
=======

To use an operator, you have to include the class first.

.. code-block:: c++

    #include "cppitasc/utils/operator.hpp"

**Inside the** ``init()`` **function**

Extract the operator name from the .xml parameter and save it inside a string.

.. code-block:: c++

    string operator_name_;  //class variable
    extract(params["operator"], operator_name_);

Create an operator object by giving it the threshold and a operator name.

.. code-block:: c++

    Operator<double> operator;  //class variable
    operator = Operator<double>(threshold, operator_name_)

**Inside the** ``onStart()`` **function**

Reset the operator when the component is started.

.. code-block:: c++

    operator.reset();

**Inside the** ``onUpdate()`` **function**

Check if the condition is met.

.. code-block:: c++

    auto result = operator.check(current_value);
