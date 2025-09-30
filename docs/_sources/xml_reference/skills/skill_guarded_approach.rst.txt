======================
skill_guarded_approach
======================

A skill that moves along a fixed frame axis until it measures a certain force

Defined at line 10 of file :doc:`skills/skill_guarded_approach.xml <../model_files/pitasc_library/skills/skill_guarded_approach_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, force_controlled

  | **Prototypes**
  |   :doc:`skill_concurrency`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame.

  | **control_frame** : string
  |  Name of the frame that defines the direction of motion.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **max_forces** : csv:float
  |  Forces in [N].
  |  **Default**: 10.0

  | **axes** : csv:string
  |  The direction of motion. Can be multiple axes.
  |  **Default**: x

  | **velocities** : csv:float
  |  Velocities in [m/s].
  |  **Default**: 0.01

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
  |  **Default**: odict_keys(['force_threshold'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **skills** : list:skill
  |  Sub-skills that are executed simultaneously.
  |  **Default**: odict_keys(['move_skill', 'hold_skill', 'force_skill'])

  | **move_skill** : :doc:`skill_cartesian_velocity`
  |  Track a desired velocity of tool_frame w.r.t. target_frame.
  |  
  |  For Translation, target_frame specifies the translation axes. For Rotation, tool_frame specifies the pivot point. Specifying the rotation axes with target_frame does not fully work (see #356)

  | **hold_skill** : :doc:`skill_hold_pose`
  |  Hold the position/orientation on selected axes.

  | **force_skill** : :doc:`skill_force`
  |  Models a loop for force control

Examples
========

**skill_guarded_approach** is used in the following examples:

* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/dual_robot/dual_robot_forces_xml`
* :doc:`../examples/monitors/multiple_events_in_same_skill_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/scripts/logging_xml`
