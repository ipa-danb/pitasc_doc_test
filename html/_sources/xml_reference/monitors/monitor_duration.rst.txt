================
monitor_duration
================

Triggers after a certain time.

Defined at line 106 of file :doc:`monitors/basic.xml <../model_files/pitasc_library/monitors/basic_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   logic

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **duration** : float
  |  The amount of time to wait until triggering

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

Examples
========

**monitor_duration** is used in the following examples:

* :doc:`../examples/beginner/forces_feedforward_xml`
* :doc:`../examples/beginner/forces_xml`
* :doc:`../examples/beginner/move_math_parser_xml`
* :doc:`../examples/beginner/simple_count_xml`
* :doc:`../examples/beginner/skill_concurrency_xml`
* :doc:`../examples/beginner/track_frame_500hz_xml`
* :doc:`../examples/beginner/track_frame_xml`
* :doc:`../examples/dual_robot/bounds_dual_robot_xml`
* :doc:`../examples/monitors/sync_xml`
* :doc:`../examples/rosless/forces_rosless_xml`
* :doc:`../examples/scripts/temp_frame_xml`
* :doc:`../examples/skills/bound_example_xml`
* :doc:`../examples/skills/forces_pid_xml`
* :doc:`../examples/skills/position_pid_xml`
