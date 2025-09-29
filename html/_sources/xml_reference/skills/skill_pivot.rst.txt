===========
skill_pivot
===========

Rotates while pushing

Defined at line 10 of file :doc:`skills/skill_pivot.xml <../model_files/pitasc_library/skills/skill_pivot_xml>` in package **pitasc_library**.

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
  |  Name of the tool frame

  | **control_frame** : string
  |  Name of the frame that defines the direction of rotation and forces

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **force_axes** : csv:string
  |  List of axes.
  |  **Default**: y, z

  | **target_forces** : csv:float
  |  Forces and torques to be applied. Must be the same number of values as for 'axes'.
  |  **Default**: 5.0, 5.0

  | **compliance** : float
  |  Force controller gain
  |  **Default**: 0.002

  | **corner_frequency** : float
  |  Force controller corner frequency
  |  **Default**: 5.0

  | **rotation_axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: a

  | **rotation_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'. If no value is provided, 0 is used for all axes.

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

  | **skills** : list:skill
  |  Sub-skills that are executed simultaneously.
  |  **Default**: odict_keys(['force', 'rotation', 'hold'])

  | **force** : :doc:`skill_apply_force`
  |  Applies a force in the direction of a frame

  | **rotation** : :doc:`skill_lin`
  |  Aligns the tool frame with a target frame

  | **hold** : :doc:`skill_hold_pose`
  |  Hold the position/orientation on selected axes.

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.

  | **tasks** : list:task
  |  Contains the task description(s).

Examples
========
No examples found that make use of **skill_pivot**