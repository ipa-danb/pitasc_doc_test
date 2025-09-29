======================
skill_ptp_time_optimal
======================

Keeps on tracking a joint configuration using a time-optimal trajectory

Defined at line 8 of file :doc:`skills/skill_ptp_time_optimal.xml <../model_files/pitasc_library/skills/skill_ptp_time_optimal_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_joint_space`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **target_joint_state** : csv:float
  |  Joint values of the target pose.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **joint_names** : csv:string
  |  Joint names of the target pose.

  | **trajectory_duration** : float
  |  Duration of the trajectory in [s]; '0' means as fast as possible. The realized duration can be longer if the original value conflicts with maximal velocity.
  |  **Default**: False

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.0

  | **max_angular_acceleration** : float
  |  Max angular acceleration.
  |  **Default**: 1.0

  | **joint_positioning_accuracy** : csv:float
  |  Threshold around the target joint state to consider it reached by the robot. One entry for all OR one entry for each joint.
  |  **Default**: 0.01

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
  |  Specifies the angular controller gain for joint position control.
  |  **Default**: 3.0

  | **angular_ff_controller_gain** : float
  |  Specifies the angular velocity-feed-forward controller gain for joint position control.
  |  **Default**: 0.7

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

Examples
========
No examples found that make use of **skill_ptp_time_optimal**