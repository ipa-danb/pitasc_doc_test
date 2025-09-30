========================
skill_cartesian_tracking
========================

Keeps on aligning the tool frame with a target frame

Defined at line 8 of file :doc:`skills/skill_cartesian_tracking.xml <../model_files/pitasc_library/skills/skill_cartesian_tracking_xml>` in package **pitasc_library**.

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

  | **target_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'. If no value is provided, 0 is used for all axes.

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 1.0

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.5

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **trajectory_duration** : float
  |  Duration of the trajectory in [s]. '0' means as fast as possible. Is expanded accordingly if in conflict with maximal linear veloctiy.
  |  **Default**: False

  | **linear_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian positions (i.e. x,y and z).
  |  **Default**: 3.0

  | **angular_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian angles (i.e. a,b and c).
  |  **Default**: 3.0

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['collection', 'target_to_tool'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

  | **tasks** : list:task
  |  Contains the task description(s).
  |  **Default**: odict_keys(['tracking'])

Examples
========

**skill_cartesian_tracking** is used in the following examples:

* :doc:`../examples/beginner/move_math_parser_xml`
* :doc:`../examples/beginner/skill_concurrency_xml`
* :doc:`../examples/beginner/track_frame_500hz_xml`
* :doc:`../examples/beginner/track_frame_xml`
* :doc:`../examples/monitors/geometry_xml`
* :doc:`../examples/monitors/user_confirm_xml`
* :doc:`../examples/scripts/temp_frame_xml`
