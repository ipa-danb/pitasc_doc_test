========================
skill_cartesian_velocity
========================

Track a desired velocity of tool_frame w.r.t. target_frame.

For Translation, target_frame specifies the translation axes. For Rotation, tool_frame specifies the pivot point. Specifying the rotation axes with target_frame does not fully work (see #356)

Defined at line 8 of file :doc:`skills/skill_cartesian_velocity.xml <../model_files/pitasc_library/skills/skill_cartesian_velocity_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, velocity_controlled

  | **Prototypes**
  |   :doc:`skill_cartesian`, :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame

  | **axes** : csv:string
  |  List of axes to apply velocities.
  |  **Default**: x, y, z, a, b, c

  | **velocities** : csv:float
  |  Velocities in [m/s] or [rad/s].
  |  **Default**: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

  | **velocity_frame** : string
  |  Defines in which direction the robot will move.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

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

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['collection', 'target_to_tool'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

  | **tasks** : list:task
  |  Contains the task description(s).
  |  **Default**: odict_keys(['velocity_feedforward'])

  | **target_frame** : string
  |  Name of the target frame

Examples
========

**skill_cartesian_velocity** is used in the following examples:

* :doc:`../examples/beginner/skill_concurrency_xml`
