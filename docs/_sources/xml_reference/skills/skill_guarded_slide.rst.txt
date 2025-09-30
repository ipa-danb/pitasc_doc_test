===================
skill_guarded_slide
===================

A skill that moves along a fixed frame axis until it measures a certain force

Defined at line 8 of file :doc:`skills/skill_guarded_slide.xml <../model_files/pitasc_library/skills/skill_guarded_slide_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, force_controlled

  | **Prototypes**
  |   :doc:`skill_slide`, :doc:`skill_concurrency`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **control_frame** : string
  |  Name of the frame that defines the direction of motion.

  | **tool_frame** : string
  |  Name of the tool frame.

  | **move_axes** : csv:string
  |  List of axes to apply velocities.

  | **velocities** : csv:float
  |  Velocities in [m/s] or [rad/s].

  | **force_axes** : csv:string
  |  List of axes.

  | **target_forces** : csv:float
  |  Forces and torques to be applied. Must be the same number of values as for 'axes'.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **compliance** : float
  |  Force controller gain
  |  **Default**: 0.002

  | **corner_frequency** : float
  |  Force controller corner frequency
  |  **Default**: 5.0

  | **max_forces** : csv:float
  |  Force in move direction that stops the slide.
  |  **Default**: 10.0

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.
  |  **Default**: odict_keys(['monitor_threshold'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **skills** : list:skill
  |  Sub-skills that are executed simultaneously.
  |  **Default**: odict_keys(['move', 'force', 'hold'])

  | **move** : :doc:`skill_cartesian_velocity`
  |  Track a desired velocity of tool_frame w.r.t. target_frame.
  |  
  |  For Translation, target_frame specifies the translation axes. For Rotation, tool_frame specifies the pivot point. Specifying the rotation axes with target_frame does not fully work (see #356)

  | **force** : :doc:`skill_apply_force`
  |  Applies a force in the direction of a frame

  | **hold** : :doc:`skill_hold_pose`
  |  Hold the position/orientation on selected axes.

  | **operator** : string
  |  Defines the stop condition.
  |  **Default**: absolute_greater

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.

  | **tasks** : list:task
  |  Contains the task description(s).

Examples
========

**skill_guarded_slide** is used in the following examples:

* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/scripts/temp_frame_xml`
