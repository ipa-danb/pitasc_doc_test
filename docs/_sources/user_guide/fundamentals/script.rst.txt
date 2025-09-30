=======
Scripts
=======

Scripts contain C++ code to fulfill more complex and application-specific functions required by the user. They attach to a skill and
run in parallel with it. They enable, among other things, the interaction with hardware and software components, like grippers, plcs, ros nodes, etc.

Defined at file ``models/coordination.xml`` in package **pitasc_library**.

**General structure**
---------------------

**xml**

Chain of prototype based inheritance

.. code-block::

    any_script --> script --> object --> dictionary --> base --> descriptive

All scripts are inheriting from 'script'.

Scripts contain the following attributes inside the ``<type>`` tag.

.. list-table:: Attributes inside ``<type>`` tag
   :widths: auto
   :header-rows: 1

   * - Attribute
     - Description

   * - id
     - Name of the script, e.g. "my_script". Needs to be locally unique to allow identification. If not unique, a incrementing element e.g., "_no0", "_no1", "_no2", ... will be added
   * - data_type
     - Already set by inheritance (dict)
   * - prototype
     - The base type the script "inherits" from, e.g. "script".

|

Scripts contain the following parameters inside the ``<meta>`` tag by default.

.. list-table:: Members inside ``<meta>`` tag
   :widths: auto
   :header-rows: 1

   * - Member
     - Description

   * - description     
     - Describes the script
   * - implementation  
     - Implementation details (links to the cpp class)
   * - categories      
     - Categories the script is part of (e.g., logging, io, ..)
   * - visibility      
     - Visibility of the script (one of: required, basic, expert, hidden)

|

The xml definition of a script basically looks like the following:

.. code-block:: xml

    <type id= '{Choose unique id}' prototype= '{Add parent script id}'> <!-- reference here -->
        <meta>
            <member id="description"> {Choose meaningful description} </member>
            <member id="categories"> {Add category(s) separated by comma} <member>
            <member id="visibility"> {Choose enum} </member>
            <member id="implementation">
                <clone prototype="orocos">
                    <member id="package"> {Add cpp library name} </member>
                    <member id="component"> {Add name of the class from .cpp file} </member>
                </clone>
            </member>
        </meta>
    </type>

(``cpp library name`` could for example be  ``cppitasc_scripts``.)


.. note::
    See also :doc:`../how-to/advanced/How_to_create_a_custom_script`
