====================
skill_slide_relative
====================

Slides to a target relative to the current position

Defined at line 10 of file :doc:`skills/skill_slide_relative.xml <../model_files/pitasc_library/skills/skill_slide_relative_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, force_controlled

  | **Prototypes**
  |   :doc:`skill_concurrency`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **control_frame** : string
  |  Name of the frame that defines the direction of motion.

  | **tool_frame** : string
  |  Name of the tool frame.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **move_axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **target_offsets** : csv:float
  |  Relative slide target offsets. Must be the same number of values as for 'axes'. If no value is provided, 0 is used for all axes.

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 1.0

  | **force_axes** : csv:string
  |  List of axes.
  |  **Default**: x, z

  | **target_forces** : csv:float
  |  Forces and torques to be applied. Must be the same number of values as for 'axes'.
  |  **Default**: 0.0, 0.0

  | **compliance** : float
  |  Force controller gain
  |  **Default**: 0.002

  | **corner_frequency** : float
  |  Force controller corner frequency
  |  **Default**: 5.0

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
  |  **Default**: odict_keys(['force', 'position'])

  | **force** : :doc:`skill_apply_force`
  |  Applies a force in the direction of a frame

  | **position** : :doc:`skill_relative_lin`
  |  Aligns the tool with an offset relative to the current pose

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.

  | **tasks** : list:task
  |  Contains the task description(s).

Examples
========
No examples found that make use of **skill_slide_relative**