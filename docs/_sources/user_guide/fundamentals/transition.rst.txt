===========
Transitions
===========

A transition defines the change to the next skill when the current skill ends. Transitions get triggered by an event and link to a followup skill. This can
be a useful tool to create, for example, loops or other kinds of control flow.

Within a ``skill_sequence``, all skills already automatically transition to the next following skill.

Defined at file ``models/coordination.xml`` in package **pitasc_library**.

**General structure**
---------------------

**xml**

Chain of prototype based inheritance

.. code-block:: text

    any_transition¹--> transition --> dictionary --> base --> descriptive

All transitions are inheriting from 'transition'.

Transitions contain the following attributes inside the ``<type>`` tag.

.. list-table:: Attributes inside ``<type>`` tag
   :widths: auto
   :header-rows: 1

   * - Attribute
     - Description

   * - id
     - Name of the transition, e.g. "my_transition". Needs to be locally unique to allow identification. If not unique, a incrementing element e.g., "_no0", "_no1", "_no2", ... will be added
   * - data_type
     - Already set by inheritance (dict)
   * - prototype
     - The base type the transition "inherits" from, e.g. "transition".

|

Transitions contain the following parameters inside the ``<meta>`` tag by default.

.. list-table:: Members inside ``<meta>`` tag
   :widths: auto
   :header-rows: 1

   * - Member
     - Description

   * - description     
     - Describes the transition
   * - visibility      
     - Visibility of the transition (one of: required, basic, expert, hidden)

|

Transitions contain the following parameters inside the ``<data>`` tag by default.

.. list-table:: Members inside ``<data>`` tag
   :widths: 25 25
   :header-rows: 1

   * - Member
     - Description

   * - event
     - Name of the event that triggers the transition.
   * - target
     - Id of the target skill (skill that gets transitioned to).

|

The xml definition of a transition basically looks like the following:

.. code-block:: xml

    <type id= '{Choose unique id}' prototype= '{Add parent transition id}'> <!-- reference here -->
        <meta>
            <member id="description"> {Choose meaningful description} </member>
            <member id="visibility"> {Choose enum} </member>
        </meta>
        <data>
            <member id="event"> {Choose event name} </member>
            <member id="target"> {Choose target name} </member>
        </data>
    </type>
