=================
skill_partial_lin
=================

A skill that moves to a target frame only in specified axes and holds the other axes in place

Defined at line 10 of file :doc:`skills/skill_partial_lin.xml <../model_files/pitasc_library/skills/skill_partial_lin_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_concurrency`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame.

  | **target_frame** : string
  |  Name of the target frame.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **target_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'.
  |  **Default**: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 1.0

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.5

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.

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

  | **skills** : list:skill
  |  Sub-skills that are executed simultaneously.
  |  **Default**: odict_keys(['lin_skill', 'hold_skill'])

  | **thresholds** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'.
  |  **Default**: 0.001, 0.001, 0.001, 0.005, 0.005, 0.005

  | **linear_controller_gain** : float
  |  Equivalent proportional controller in linear region.
  |  **Default**: 3.0

  | **angular_controller_gain** : float
  |  Equivalent proportional controller in angular region.
  |  **Default**: 3.0

  | **lin_skill** : :doc:`skill_lin`
  |  Aligns the tool frame with a target frame

  | **hold_skill** : :doc:`skill_hold_pose`
  |  Hold the position/orientation on selected axes.

Examples
========

**skill_partial_lin** is used in the following examples:

* :doc:`../examples/beginner/skill_sequence_xml`
* :doc:`../examples/skills/partial_lin_xml`
