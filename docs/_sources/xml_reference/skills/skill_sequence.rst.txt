==============
skill_sequence
==============

List of skills which are executed in sequence.

Defined at line 172 of file :doc:`models/coordination.xml <../model_files/pitasc_library/models/coordination_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   composition

  | **Prototypes**
  |   skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **skills** : list:skill
  |  Sub-skills that are executed in sequence.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

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

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **initial_skill** : string
  |  First skill to run.

Examples
========

**skill_sequence** is used in the following examples:

* :doc:`../examples/advanced/strings_xml`
* :doc:`../examples/beginner/forces_feedforward_xml`
* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/beginner/free_drive_xml`
* :doc:`../examples/beginner/move_math_parser_xml`
* :doc:`../examples/beginner/multiple_apps_xml`
* :doc:`../examples/beginner/rosservice_calls_xml`
* :doc:`../examples/beginner/scrollable_multiple_apps_xml`
* :doc:`../examples/beginner/simple_count_xml`
* :doc:`../examples/beginner/simple_idle_xml`
* :doc:`../examples/beginner/simple_move_xml`
* :doc:`../examples/beginner/skill_concurrency_xml`
* :doc:`../examples/beginner/skill_parallel_xml`
* :doc:`../examples/beginner/skill_sequence_xml`
* :doc:`../examples/beginner/track_frame_500hz_xml`
* :doc:`../examples/beginner/track_frame_xml`
* :doc:`../examples/beginner/transitions_xml`
* :doc:`../examples/customized_robots/linear_axis_xml`
* :doc:`../examples/customized_robots/mimic_gripper_xml`
* :doc:`../examples/dual_robot/bounds_dual_robot_xml`
* :doc:`../examples/dual_robot/dual_robot_forces_xml`
* :doc:`../examples/dual_robot/simple_dual_robot_xml`
* :doc:`../examples/monitors/geometry_xml`
* :doc:`../examples/monitors/io_xml`
* :doc:`../examples/monitors/measurements_xml`
* :doc:`../examples/monitors/multiple_events_in_same_skill_xml`
* :doc:`../examples/monitors/sync_xml`
* :doc:`../examples/monitors/user_confirm_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/rosless/simple_move_rosless_xml`
* :doc:`../examples/scripts/frame_editor_xml`
* :doc:`../examples/scripts/io_xml`
* :doc:`../examples/scripts/logging_xml`
* :doc:`../examples/scripts/temp_frame_xml`
* :doc:`../examples/skills/blacklist_xml`
* :doc:`../examples/skills/bound_example_xml`
* :doc:`../examples/skills/conical_helix_xml`
* :doc:`../examples/skills/cylindrical_helix_xml`
* :doc:`../examples/skills/forces_pid_xml`
* :doc:`../examples/skills/lin_time_optimal_xml`
* :doc:`../examples/skills/lin_trajectory_xml`
* :doc:`../examples/skills/partial_lin_xml`
* :doc:`../examples/skills/position_pid_xml`
* :doc:`../examples/skills/ptp_trajectory_xml`
* :doc:`../examples/skills/spherical_velocity_xml`
