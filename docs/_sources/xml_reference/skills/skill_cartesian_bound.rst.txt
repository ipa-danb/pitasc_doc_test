=====================
skill_cartesian_bound
=====================

Bound for a cartesian value

Defined at line 8 of file :doc:`skills/skill_cartesian_bound.xml <../model_files/pitasc_library/skills/skill_cartesian_bound_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_cartesian`, :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

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

  | **axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **upper_bound** : csv:float
  |  List of upper bound values respective to axes.
  |  **Default**: 10.0, 10.0, 10.0, 3.14, 3.14, 3.14

  | **lower_bound** : csv:float
  |  List of lower bound values respective to axes.
  |  **Default**: -10.0, -10.0, -10.0, -3.14, -3.14, -3.14

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **tasks** : list:task
  |  Contains the task description(s).

  | **bounds** : list:bound
  |  Contains the bounds description(s).
  |  **Default**: odict_keys(['tracking_bound'])

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **scaler** : float
  |  Time constant restricting the movement, i.e.,  v_allowed <  (p_bound - p_current) / scalar
  |  **Default**: 1.0

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['collection', 'target_to_tool'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========

**skill_cartesian_bound** is used in the following examples:

* :doc:`../examples/dual_robot/bounds_dual_robot_xml`
* :doc:`../examples/skills/bound_example_xml`
