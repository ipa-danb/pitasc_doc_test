========
Monitors
========

A monitor is a stop condition that is attached to a skill. In each pitasc cycle (update step), it checks its condition, which can be
the successful completion of the task or an error in the middle of execution. If the condition is met, an so-called *event* is
triggered which can be used to transition to the next skill. A monitor can surveil forces, movement distances along axis, rotation angles around axis and more. For example, a monitor can be used to surveil the traveled distance in z-direction, i.e., when the robot has moved for example 10 mm, pitasc executes the next skill.

Defined at file ``models/coordination.xml`` in package **pitasc_library**.

**General structure**
---------------------

**xml**

Chain of prototype based inheritance

.. code-block::

    any_monitor --> monitor --> object --> dictionary --> base --> descriptive

All monitors are inheriting from 'monitor'.

Monitors contain the following attributes inside the ``<type>`` tag.

.. cell table width fucked up: https://github.com/readthedocs/sphinx_rtd_theme/issues/1505

.. list-table:: Attributes inside ``<type>`` tag
   :widths: auto
   :header-rows: 1

   * - Attribute
     - Description

   * - id
     - Name of the monitor, e.g. "my_monitor". Needs to be locally unique to allow identification. If not unique, a incrementing element e.g., "_no0", "_no1", "_no2", ... will be added
   * - data_type
     - Already set by inheritance (dict)
   * - prototype
     - The base type the monitor "inherits" from, e.g. "monitor".

|

Monitors contain the following parameters inside the ``<meta>`` tag by default.

.. list-table:: Members inside ``<meta>`` tag
   :widths: auto
   :header-rows: 1

   * - Member
     - Description

   * - description     
     - Describes the monitor
   * - implementation  
     - Implementation details (links to the cpp class)
   * - categories      
     - Categories the monitor is part of (e.g., geometry, io, ..)
   * - visibility      
     - Visibility of the monitor (one of: required, basic, expert, hidden)

|

Monitors contain the following parameters inside the ``<data>`` tag by default.

.. list-table:: Members inside ``<data>`` tag
   :widths: 25 25
   :header-rows: 1

   * - Member
     - Description

   * - event
     - Primary event, that is triggered by the monitor (Default: succeeded)

|

The xml definition of a monitor basically looks like the following:

.. code-block:: xml

    <type id= '{Choose unique id}' prototype= '{Add parent monitor id}'> <!-- reference here -->
        <meta>
            <member id="description"> {Choose meaningful description} </member>
            <member id="categories"> {Add category(s) separated by comma} <member>
            <member id="visibility"> {Choose enum} </member>
            <member id="implementation">
                <clone prototype="orocos">
                    <member id="package"> {Add cpp library name}  </member>
                    <member id="component"> {Add monitor cpp class name} </member>
                </clone>
            </member>
        </meta>
        <data>
            <member id="event"> {Choose event name} </member>
        </data>
    </type>

For example, the definition of a ``monitor_duration`` looks like this:

.. code-block:: xml

    <type id="monitor_duration" prototype="monitor">
        <meta>
            <member id="description">Triggers after a certain time.</member>
            <member id="categories">logic</member>
            <member id="implementation">
                <clone prototype="orocos">
                    <member id="package">cppitasc_monitors</member>
                    <member id="component">DurationMonitor</member>
                </clone>
            </member>
        </meta>
        <data>
            <type id="duration" prototype="float_parameter">
                <meta>
                    <member id="description">The amount of time to wait until triggering</member>
                    <member id="visibility">required</member>
                </meta>
            </type>
        </data>
    </type>


.. note::
    See also :doc:`../how-to/advanced/How_to_create_a_custom_monitor`





