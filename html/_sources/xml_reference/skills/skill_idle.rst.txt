==========
skill_idle
==========

A skill that does nothing

Defined at line 8 of file :doc:`skills/skill_idle.xml <../model_files/pitasc_library/skills/skill_idle_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, logic

  | **Prototypes**
  |   skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

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

Examples
========

**skill_idle** is used in the following examples:

* :doc:`../examples/beginner/scrollable_multiple_apps_xml`
* :doc:`../examples/beginner/simple_count_xml`
* :doc:`../examples/beginner/skill_parallel_xml`
* :doc:`../examples/monitors/io_xml`
* :doc:`../examples/monitors/switch_skill_with_rosservice_xml`
* :doc:`../examples/monitors/sync_xml`
* :doc:`../examples/scripts/io_xml`
