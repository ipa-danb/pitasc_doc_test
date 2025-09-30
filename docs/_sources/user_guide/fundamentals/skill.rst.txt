======
Skills
======

A skill is a subtask of a robot program application. In its simplest version a skill consists only of one of pitasc's basic skill types, e.g. a **skill_lin**: move linearly from point A to point B. But a skill can also be composed out of multiple skills to create a more complex compound skill. Skills are also able to inherit from other skills.

Defined at file ``models/coordination.xml`` in package **pitasc_library**.

**General structure**
---------------------

Chain of prototype based inheritance

.. code-block:: text

    any_skills --> (skill_single_robot) --> skill --> object --> dictionary --> base --> descriptive

All skills are inheriting from 'skill', but most skills are inheriting from 'skill_single_robot'.

Skills contain the following attributes inside the ``<type>`` tag.


.. list-table:: Attributes inside ``<type>`` tag
   :widths: auto
   :header-rows: 1

   * - Attribute
     - Description

   * - id
     - Needs to be locally unique to allow identification. If not unique, a incrementing element e.g., "_no0", "_no1", "_no2", ... will be added
   * - data_type
     - Already set by inheritance (dict)
   * - prototype
     - The base type the skill "inherits" from, e.g. "skill_cartesian".

|

Skills contain the following parameters inside the ``<meta>`` tag.


.. list-table:: Members inside ``<meta>`` tag
   :widths: auto
   :header-rows: 1

   * - Member
     - Description

   * - description
     - Describes the function of the skill.
   * - implementation
     - Implementation details already set by inheritance.
   * - categories
     - Categories the skill is part of (e.g. single_robot, dual_robot, position_controlled, force_controlled, velocity_controlled).
   * - visibility
     - Visibility of the skill (enum: required, basic, expert, hidden).

|

Skills contain the following parameters inside the ``<data>`` tag.

.. list-table:: Members inside ``<data>`` tag
   :widths: auto
   :header-rows: 1

   * - Member
     - Description

   * - skill_name
     - Name of this skill. It must be locally unique.
   * - monitors
     - Contains the monitors of the skill that determine when the skill should terminate.
   * - transitions
     - Contains additional transitions to other states (skills), given an event name.
   * - scripts
     - Contains scripts that should be executed while the skill is active.

   * - collections
     - Contains the kinematic chains of the skill (feature, robot, object chains).
   * - loops
     - Contains the kinematic loop(s) that define the task to be solved.
   * - tasks
     - Contains the task description(s).
   * - bounds
     - Contains the bounds description(s).


For more information on the expert parameters, see `A Prototype-Based Skill Model for Specifying Robotic Assembly Tasks <https://doi.org/10.1109/ICRA.2018.8462885>`_.


The xml definition of a skill basically looks like the following:

.. code-block:: xml

    <type id= '{Choose unique id}' prototype= '{Add parent skill id}'> <!-- reference here -->
        <meta>
            <member id="description"> {Choose meaningful description} </member>
            <member id="categories"> {Add category(s) separated by comma} </member>
            <member id="visibility"> {Choose enum} </member>
        </meta>
        <data>
            <member id="skill_name"> {Choose name} </member>
            <member id="collections"> {Add collection element(s)} </member>
            <member id="loops"> {Add loop element(s)} </member>
            <member id="tasks"> {Add task element(s)} </member>
            <member id="bounds"> {Add bound element(s)} </member>
            <member id="monitors"> {Add monitor element(s)} </member>
            <member id="transitions"> {Add transition element(s)} </member>
            <member id="scripts"> {Add script element(s)} </member>
        </data>
    </type>


For example, a skill which moves the tool frame along three waypoints to form a triangle could look like this:

.. code-block:: xml

    <pitasc>
        <models>
            <include package="pitasc_library" file="models/pitasc.xml"/>
            <include package="pitasc_library" file="skills/skill_lin.xml"/>

            <type id="skill_move_triangle" prototype="skill_sequence">
                <meta>
                    <member id="description">Moves along the given three frames to form a triangle</member>
                    <member id="categories">single_robot, position_controlled</member>
                    <member id="visibility">basic</member>
                </meta>

                <data>

                    <type id="tool_frame" prototype="frame">
                        <meta>
                            <member id="description">Name of the tool frame</member>
                            <member id="visibility">required</member>
                        </meta>
                    </type>

                    <type id="frame_1" prototype="frame">
                        <meta>
                            <member id="description">Name of the first frame</member>
                            <member id="visibility">required</member>
                        </meta>
                    </type>

                    <type id="frame_2" prototype="frame">
                        <meta>
                            <member id="description">Name of the second frame</member>
                            <member id="visibility">required</member>
                        </meta>
                    </type>
                    
                    <type id="frame_1" prototype="frame">
                        <meta>
                            <member id="description">Name of the third frame</member>
                            <member id="visibility">required</member>
                        </meta>
                    </type>

                    <member id="skills">
                        <clone prototype="skill_lin">
                            <member id="tool_frame" reference_id="tool_frame" />
                            <member id="target_frame" reference_id="frame_1" />
                        </clone>
                        <clone prototype="skill_lin">
                            <member id="tool_frame" reference_id="tool_frame" />
                            <member id="target_frame" reference_id="frame_2" />
                        </clone>
                        <clone prototype="skill_lin">
                            <member id="tool_frame" reference_id="tool_frame" />
                            <member id="target_frame" reference_id="frame_3" />
                        </clone>
                        <clone prototype="skill_lin">
                            <member id="tool_frame" reference_id="tool_frame" />
                            <member id="target_frame" reference_id="frame_1" />
                        </clone>
                    </member>

                </data>
            </type>
        </models>
    </pitasc>


.. note::
    See also :doc:`../how-to/advanced/How_to_create_a_custom_skill`