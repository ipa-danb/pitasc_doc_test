==========
skill_push
==========

A skill that pushes and keeps the position

Defined at line 10 of file :doc:`skills/skill_push.xml <../model_files/pitasc_library/skills/skill_push_xml>` in package **pitasc_library**.

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

  | **force_frame** : string
  |  Name of the frame that defines the direction of motion.

  | **axes** : csv:string
  |  List of axes.

  | **target_forces** : csv:float
  |  Forces and torques to be applied. Must be the same number of values as for 'axes'.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **compliance** : float
  |  A floating point number parameter
  |  **Default**: 0.002

  | **corner_frequency** : float
  |  A floating point number parameter
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
  |  **Default**: odict_keys(['force', 'hold'])

  | **force** : :doc:`skill_apply_force`
  |  Applies a force in the direction of a frame

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

**skill_push** is used in the following examples:

* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/scripts/temp_frame_xml`
