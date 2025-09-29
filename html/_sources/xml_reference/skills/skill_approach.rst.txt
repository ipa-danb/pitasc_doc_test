==============
skill_approach
==============

A skill approaching a target frame in two steps

Defined at line 9 of file :doc:`skills/skill_approach.xml <../model_files/pitasc_library/skills/skill_approach_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_sequence`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame.

  | **target_frame** : string
  |  Name of the target frame.

  | **approach_offsets** : csv:float
  |  Offsets of the axes during the approach. Must be the same number of values as for 'axes'. If no value is provided, 0 is used for all axes.
  |  **Default**: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **target_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'. If no value is provided, 0 is used for all axes.
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

  | **initial_skill** : string
  |  First skill to run.

  | **skills** : list:skill
  |  Sub-skills that are executed in sequence.
  |  **Default**: odict_keys(['approach', 'target'])

  | **linear_controller_gain** : float
  |  Equivalent proportional controller in linear region.
  |  **Default**: 3.0

  | **angular_controller_gain** : float
  |  Equivalent proportional controller in linear region.
  |  **Default**: 3.0

  | **approach** : :doc:`skill_lin`
  |  Aligns the tool frame with a target frame

  | **target** : :doc:`skill_lin`
  |  Aligns the tool frame with a target frame

Examples
========

**skill_approach** is used in the following examples:

* :doc:`../examples/beginner/multiple_apps_xml`
* :doc:`../examples/beginner/scrollable_multiple_apps_xml`
* :doc:`../examples/beginner/skill_sequence_xml`
