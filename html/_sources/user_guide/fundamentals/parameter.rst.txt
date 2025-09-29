==========
Parameters
==========

Skills, scripts, monitors, even the application, everything is a parameter. By inheriting from other parameters and
including sub-parameters inside them, everything is able to be represented.

Defined at file ``models/parameters.xml`` in package **pitasc_library**.


**General structure**
---------------------

Chain of prototype based inheritance. *base* is the basic parameter prototype, which contains the meta data *description* and *visibility*.

.. code-block::

    any_parameter --> base --> descriptive

All parameters are inheriting from 'base'.

Basic parameters contain the following attributes inside the ``<type>`` tag.

.. list-table:: Attributes inside ``<type>`` tag
   :widths: auto
   :header-rows: 1

   * - Attribute
     - Description

   * - id
     - Needs to be locally unique to allow identification, If not unique, a incrementing element e.g., "_no0", "_no1", "_no2", ... will be added
   * - data_type
     - Data type of the parameter, can't be changed once set
   * - prototype
     - The base type the parameter "inherits" from, e.g. "string_parameter".

|

Basic parameters contain the following parameters inside the ``<meta>`` tag by default.

.. list-table:: Members inside ``<meta>`` tag
   :widths: auto
   :header-rows: 1

   * - description
     - Description of the parameter
   * - visibility
     - Visibility of the parameter (one of: required, basic, expert, hidden)

|

The xml definition of a parameter basically looks like the following:

.. code-block:: xml

    <type id="{Choose unique id}" prototype="{Add parent id}" data_type="{Choose data type}">  <!-- reference would be added here -->
        <meta>
            <member id="description"> {Choose meaningful description} </member>
            <member id="visibility"> {Choose enum} </member>
        </meta>
        <data> {data depending on parameter type} </data>
    </type>


For example, this is the definition of a frame parameter (from the pitasc library):

.. code-block:: xml

    <type id="frame" prototype="string_parameter">
        <meta>
            <member id="description">A frame (coordinate system)</member>
            <clone prototype="restrictions">
                <clone prototype="blacklist"> </clone>
            </clone>
        </meta>
    </type>


The blacklist restriction with a space defines that the value of the parameter must not be empty. See below for more information on restrictions.


**data_type vs prototype**
--------------------------------
*data_type* describes the actual representation of the data of the parameter. It can only be one of the following:

- int
- bool
- float
- string
- csv:int, csv:bool, csv:float, csv:string
- dict
- list:{parameter type} ({parameter type can be any pitasc parameter type, e.g. list:frame)
- parameter (this is basically saying "don't know yet, will be defined in inherting parameters")
- parameter:{parameter type} ({parameter type can be any pitasc parameter type, e.g. parameter:monitor)

*prototype* needs to be an existing pitasc parameter type, defined with ``<type id="..."``. Usually a pitasc parameter type sets the *data_type* already, so if you derive from anything else than ``prototype="base"``, you do not need to set the *data_type*. However if you want to set it, e.g., because you want to create a parameter containing a list of frames, you need to set it and set the prototype to *base* (``data_type="list:frame" prototype="base"``)


**Parameter basic types**
-------------------------
Basic type parameters can be used though inheritance. The following parameter basic types are available.

.. list-table:: List of basic parameter prototypes
   :widths: auto
   :header-rows: 1

   * - Prototype
     - Description

   * - bool_parameter
     - A boolean parameter
   * - int_parameter
     - An integer parameter
   * - float_parameter
     - A floating point number parameter
   * - dictionary
     - A dictionary parameter (assoziative array)

.. list-table:: List of string datatypes
   :widths: auto
   :header-rows: 1

   * - Prototype
     - Description

   * - string_like_parameter
     - A parameter that behaves like a string
   * - string_concatenation
     - A list of strings that is concatenated to a single string (children of string_like_parameter)
   * - string_parameter
     - A string parameter (children of string_like_parameter)

.. list-table:: List of string list datatypes
   :widths: auto
   :header-rows: 1

   * - Prototype
     - Description

   * - string_list_like_parameter
     - A parameter that behaves like a string or string list
   * - string_list_concatenation
     - A list of strings and string lists that is concatenated to a single string list (children of string_list_like_parameter)
   * - string_list
     - A list of strings (children of string_list_like_parameter)

.. list-table:: List of csv datatypes
   :widths: auto
   :header-rows: 1

   * - Prototype
     - Description

   * - bool_csv
     -  A comma-separated list of booleans
   * - int_csv
     -  A comma-separated list of integers
   * - float_csv
     -  A comma-separated list of floats
   * - string_csv
     -  A comma-separated list of strings


**Restrictions**
----------------

| Restrictions are used to restrict the values a parameter can assume.
| The following restrictions are available.

.. list-table:: List of possible restrictions
   :widths: auto
   :header-rows: 1

   * - Restriction type
     - Description

   * - enum
     - An enumeration of strings allowed for this parameter
   * - blacklist
     - An enumeration of strings *not* allowed for this parameter
   * - int_max
     - Upper boundary for a int parameter
   * - int_min
     - Lower boundary for a int parameter
   * - int_csv_max
     - Upper boundaries for the values of a csv int list
   * - int_csv_min
     - Lower boundaries for the values of a csv int list
   * - float_max
     - Upper boundary for a float parameter
   * - float_min
     - Lower boundary for a float parameter
   * - float_csv_max
     - Upper boundaries for the values of a csv float list
   * - float_csv_min
     - Lower boundaries for the values of a csv float list

|

Add restrictions to a parameter by adding them inside the ``<meta>`` tag.

.. code-block:: xml

    <meta>
        ...
        <clone prototype="restrictions">                        <!-- list of restrictions -->
            <clone prototype="enum">x, y, z, a, b, c</clone>    <!-- example restriction -->
        </clone>
    </meta>


**Lists & Naming**
------------------

| **Naming**
| In lists, it can happen that two elements would get the same name (id). Consider the following example:

.. code-block:: xml

    <member id="skills">
        <clone prototype="skill_lin" />
        <clone prototype="skill_lin" />
        <clone prototype="skill_lin" />
    </member>

In this case, pitasc changes the id of the skills such that they are unique. The assigned ids of the skills are then

.. code-block:: xml

    <member id="skills">
        <clone id="skill_lin" prototype="skill_lin" />
        <clone id="skill_lin_no0" prototype="skill_lin" />
        <clone id="skill_lin_no1" prototype="skill_lin" />
    </member>

| **Replacing**
| Currently, it is not possible to remove entries from a list by using xml syntax. So, if a prototype adds something to a list, e.g. a controller to `controllers`, and you want to add your own controller, you need to re-define the whole skill to have only your controller in its ``controller`` members (below ``tasks.tracking``).

.. note::
    See also :doc:`../how-to/advanced/How_to_add_a_parameter_to_a_skill_monitor_etc`