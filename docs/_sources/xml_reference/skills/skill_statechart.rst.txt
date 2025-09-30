================
skill_statechart
================

Group of skills which are connected in a state machine.

Defined at line 141 of file :doc:`models/coordination.xml <../model_files/pitasc_library/models/coordination_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   composition

  | **Prototypes**
  |   skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **initial_skill** : string
  |  First skill to run.

  | **skills** : list:skill
  |  Sub-skills that are connected in a state machine.

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

**skill_statechart** is used in the following examples:

* :doc:`../examples/beginner/skill_statechart_xml`
* :doc:`../examples/monitors/switch_skill_with_rosservice_xml`
