===============================
skill_partial_velocity_duration
===============================

A skill that moves along fixed frame axes and holds the other axes in place

Defined at line 73 of file :doc:`skills/skill_partial_velocity.xml <../model_files/pitasc_library/skills/skill_partial_velocity_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, velocity_controlled

  | **Prototypes**
  |   :doc:`skill_partial_velocity`, :doc:`skill_concurrency`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame

  | **velocity_frame** : string
  |  Defines the axes along which this skill can move.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **axes** : csv:string
  |  The directions of motion.
  |  **Default**: x

  | **velocities** : csv:float
  |  Velocities in [m/s].
  |  **Default**: 0.01

  | **duration** : float
  |  Skill duration in [s].
  |  **Default**: 1.0

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
  |  **Default**: odict_keys(['monitor_duration'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **skills** : list:skill
  |  Sub-skills that are executed simultaneously.
  |  **Default**: odict_keys(['move_skill', 'hold_skill'])

  | **move_skill** : :doc:`skill_cartesian_velocity`
  |  Track a desired velocity of tool_frame w.r.t. target_frame.
  |  
  |  For Translation, target_frame specifies the translation axes. For Rotation, tool_frame specifies the pivot point. Specifying the rotation axes with target_frame does not fully work (see #356)

  | **hold_skill** : :doc:`skill_hold_pose`
  |  Hold the position/orientation on selected axes.

Examples
========

**skill_partial_velocity_duration** is used in the following examples:

* :doc:`../examples/beginner/skill_sequence_xml`
