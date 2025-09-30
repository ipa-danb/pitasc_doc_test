==============================================
How to add a parameter to a skill, monitor, …
==============================================

Parameters are the base of everything in pitasc: skills, monitors, scripts, etc. everything is in itself a
parameter (some more complex than the others). By understanding how to add parameters, you are able to understand
how to add skills, monitors, etc. more easily.

There are three ways to add a parameter. The location where you all data is common for all the three ways.
Parameters get added inside the ``<data>`` tag of the skill, monitor, etc.

1. The default way of adding a parameter is to add it with the ``<type>`` tag.

  .. code-block:: xml

      <type id="{Choose unique id}" prototype="{Choose base type}" data_type="{Choose data type}">
          <meta>
              <member id="description"> {Choose meaningful description} </member>
              <member id="visibility"> {Choose from required, basic, expert or hidden} </member>
          </meta>
          <data> {data depending on parameter type} </data>
      </type>
  
  For more information see :doc:`../../fundamentals/parameter`

2. Apart from the creating new prototypes, editing only the ``<data>`` tag of parameters is often sufficient. For this reason, the ``<clone>`` tag is introduced. It is a short version of the syntax before and allows editing of only the inside of the ``<data>`` tag.

  .. code-block:: xml
  
      <clone id="{parameter_id}" prototype ="{parent_parameter_id}" data_type="{data_type}"> {value} </clone>

3. Another short form of the syntax on top is introduced with ``<reference>``. It is a short version to create a parameter that is a reference to another parameter.
  
  .. code-block:: xml

      <reference id="parameter" reference_id="connected_parameter"/>
