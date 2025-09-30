====================
skill_ptp_trajectory
====================

Keeps on tracking a joint configuration

Defined at line 8 of file :doc:`skills/skill_ptp_trajectory.xml <../model_files/pitasc_library/skills/skill_ptp_trajectory_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_joint_space`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **waypoints** : list:ptp_trajectory_waypoint
  |  List of joint_trajectory_waypoint to move through with blending

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **joint_names** : csv:string
  |  Joint names of the target pose.

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.0

  | **max_angular_acceleration** : float
  |  Max angular velocity.
  |  **Default**: 1.0

  | **thresholds** : csv:float
  |  Joint value thresholds. One entry for all or one entry for each joint.
  |  **Default**: 0.005

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **bounds** : list:bound
  |  Contains the bounds description(s).

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.
  |  **Default**: odict_keys(['positioning_monitor'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **angular_controller_gain** : float
  |  Specifies the approx. linear gain of the controller transfer function for the joint angles.
  |  **Default**: 3.0

  | **positioning_monitor** : **Unknown object**
  |  Checks whether the target joint state has been reached

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['base_to_eef'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

  | **tasks** : list:task
  |  Contains the task description(s).
  |  **Default**: odict_keys(['tracking'])

  | **angular_ff_controller_gain** : float
  |  Specifies the velocity feed-forward gain of the controller
  |  **Default**: 0.8

Examples
========

**skill_ptp_trajectory** is used in the following examples:

* :doc:`../examples/skills/ptp_trajectory_xml`
