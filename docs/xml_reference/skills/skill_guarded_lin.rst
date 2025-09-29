=================
skill_guarded_lin
=================

Causes a linear motion until a specified force value is reached

Defined at line 9 of file :doc:`skills/skill_guarded_lin.xml <../model_files/pitasc_library/skills/skill_guarded_lin_xml>` in package **pitasc_library**.

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

  | **target_frame** : string
  |  Name of the target frame.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **target_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'.
  |  **Default**: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 1.0

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.5

  | **max_forces** : csv:float
  |  Forces in [N].
  |  **Default**: 10.0

  | **monitor_axes** : csv:string
  |  The directions that are monitored for occuring forces (can be multiple axes).
  |  **Default**: x

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
  |  **Default**: odict_keys(['move_skill', 'force_skill'])

  | **linear_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian positions (i.e. x,y and z).
  |  **Default**: 3.0

  | **angular_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian angles (i.e. a,b and c).
  |  **Default**: 3.0

  | **move_skill** : :doc:`skill_lin`
  |  Aligns the tool frame with a target frame

  | **force_skill** : :doc:`skill_force`
  |  Models a loop for force control

Examples
========

**skill_guarded_lin** is used in the following examples:

* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
