=================
skill_cylindrical
=================

Cylindrical coordinates

Defined at line 9 of file :doc:`skills/cylindrical/skill_cylindrical.xml <../model_files/pitasc_library/skills/cylindrical/skill_cylindrical_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame

  | **target_frame** : string
  |  Name of the target frame

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **tasks** : list:task
  |  Contains the task description(s).

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['collection', 'target_to_tool'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========
No examples found that make use of **skill_cylindrical**