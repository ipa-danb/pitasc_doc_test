==================
skill_relative_ptp
==================

A skill that moves to a relative joint configuration

Defined at line 8 of file :doc:`skills/skill_relative_ptp.xml <../model_files/pitasc_library/skills/skill_relative_ptp_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_ptp`, :doc:`skill_joint_space_tracking`, :doc:`skill_joint_space`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **relative_joint_state** : csv:float
  |  Relative joint values of the target pose.

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

  | **target_joint_state** : csv:float
  |  Joint values of the target pose.

Examples
========

**skill_relative_ptp** is used in the following examples:

* :doc:`../examples/beginner/forces_feedforward_xml`
* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/beginner/simple_count_xml`
* :doc:`../examples/beginner/simple_idle_xml`
* :doc:`../examples/beginner/skill_sequence_xml`
* :doc:`../examples/customized_robots/linear_axis_xml`
* :doc:`../examples/customized_robots/mimic_gripper_xml`
* :doc:`../examples/monitors/io_xml`
* :doc:`../examples/monitors/sync_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/scripts/io_xml`
* :doc:`../examples/skills/forces_pid_xml`
* :doc:`../examples/skills/position_pid_xml`
