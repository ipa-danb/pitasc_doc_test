========================
skill_spherical_tracking
========================

Spherical coordinates

Defined at line 9 of file :doc:`skills/spherical/skill_spherical_tracking.xml <../model_files/pitasc_library/skills/spherical/skill_spherical_tracking_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_spherical`, :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

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
  |  List of axes to be aligned
  |  **Default**: phi, theta, r, a, b, c

  | **target_offsets** : csv:float
  |  Offsets of the axes to be aligned. Must be the same number of values as for 'axes'.
  |  **Default**: 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 0.5

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 2.0

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

  | **linear_controller_gain** : float
  |  Equivalent proportional controller in linear region.
  |  **Default**: 1.0

  | **angular_controller_gain** : float
  |  Equivalent proportional controller in linear region.
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

**skill_spherical_tracking** is used in the following examples:

* :doc:`../examples/skills/spherical_velocity_xml`
