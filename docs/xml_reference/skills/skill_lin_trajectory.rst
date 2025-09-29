====================
skill_lin_trajectory
====================

Moves along given blending points with blending distances to the target frame.

Care: Setting target offsets for the waypoints for orientation can cause euler angle issues.

Defined at line 150 of file :doc:`skills/skill_lin_trajectory.xml <../model_files/pitasc_library/skills/skill_lin_trajectory_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_lin_trajectory_base`, :doc:`skill_cartesian`, :doc:`loop_target`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **tool_frame** : string
  |  Name of the tool frame

  | **target_frame** : string
  |  Target frame is set automatically. Must not be overwritten!

  | **waypoints** : list:lin_trajectory_waypoint
  |  List of joint_trajectory_waypoint to move through with blending

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **axes** : csv:string
  |  List of axes to be aligned.
  |  **Default**: x, y, z, a, b, c

  | **max_linear_velocity** : float
  |  Max linear velocity.
  |  **Default**: 0.2

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.5

  | **max_linear_acceleration** : float
  |  Max linear acceleration.
  |  **Default**: 1.0

  | **max_angular_acceleration** : float
  |  Max angular acceleration. If not set, a default value (three times the linear acceleration) is used.

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **tasks** : list:task
  |  Contains the task description(s).
  |  **Default**: odict_keys(['tracking'])

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.
  |  **Default**: odict_keys(['positioning_monitor'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **linear_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian positions (i.e. x,y and z).
  |  **Default**: 3.0

  | **angular_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for Cartesian angles (i.e. a,b and c).
  |  **Default**: 3.0

  | **linear_ff_controller_gain** : float
  |  Specifies the velocity feed-forward gain of the controller
  |  **Default**: 0.8

  | **angular_ff_controller_gain** : float
  |  Specifies the velocity feed-forward gain of the controller
  |  **Default**: 0.8

  | **positioning_monitor** : :doc:`../monitors/monitor_distance`
  |  Checks whether the target frame has been reached.

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['collection', 'target_to_tool'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========

**skill_lin_trajectory** is used in the following examples:

* :doc:`../examples/skills/bound_example_xml`
* :doc:`../examples/skills/lin_trajectory_xml`
