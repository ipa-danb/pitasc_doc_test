===================
skill_hold_duration
===================

Hold the position/orientation on selected axes for duration time.

Defined at line 38 of file :doc:`skills/skill_hold_pose.xml <../model_files/pitasc_library/skills/skill_hold_pose_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_hold_pose`, :doc:`skill_cartesian_tracking`, :doc:`skill_cartesian`, :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame

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

  | **duration** : float
  |  Skill duration in [s].
  |  **Default**: 1.0

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.
  |  **Default**: odict_keys(['monitor_duration'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.
  |  **Default**: odict_keys(['script_temp_frame'])

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

  | **target_frame** : string
  |  Name of the target frame
  |  **Default**: odict_keys(['string_parameter', 'runtime_id'])

  | **prefixed_target_frame** : list:string_like_parameter
  |  A list of strings that is concatenated to a single string
  |  **Default**: odict_keys(['string_parameter', 'runtime_id'])

Examples
========

**skill_hold_duration** is used in the following examples:

* :doc:`../examples/beginner/rosservice_calls_xml`
* :doc:`../examples/beginner/skill_sequence_xml`
