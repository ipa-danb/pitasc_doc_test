=========
skill_ptp
=========

Moves the robot to a target joint configuration

Defined at line 8 of file :doc:`skills/skill_ptp.xml <../model_files/pitasc_library/skills/skill_ptp_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_joint_space_tracking`, :doc:`skill_joint_space`, skill_single_robot, skill, object, dictionary, base, descriptive

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

  | **max_angular_velocity** : float
  |  Max angular velocity.
  |  **Default**: 1.0

  | **thresholds** : csv:float
  |  Joint value thresholds. One entry for all or one entry for each joint.
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
  |  Specifies the approx. linear gain of the controller transfer function for the joint angles.
  |  **Default**: 3.0

  | **positioning_monitor** : :doc:`../monitors/monitor_control_error`
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

**skill_ptp** is used in the following examples:

* :doc:`../examples/beginner/multiple_apps_xml`
* :doc:`../examples/beginner/rosservice_calls_xml`
* :doc:`../examples/beginner/scrollable_multiple_apps_xml`
* :doc:`../examples/beginner/skill_sequence_xml`
* :doc:`../examples/beginner/skill_statechart_xml`
