=================
skill_concurrency
=================

Hierarchy of skills which are executed simultaneously.

Defined at line 203 of file :doc:`models/coordination.xml <../model_files/pitasc_library/models/coordination_xml>` in package **pitasc_library**.

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
  |  Sub-skills that are executed simultaneously.

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

**skill_concurrency** is used in the following examples:

* :doc:`../examples/beginner/forces_feedforward_xml`
* :doc:`../examples/beginner/skill_concurrency_xml`
* :doc:`../examples/dual_robot/bounds_dual_robot_xml`
* :doc:`../examples/dual_robot/simple_dual_robot_xml`
* :doc:`../examples/monitors/measurements_xml`
* :doc:`../examples/scripts/logging_xml`
* :doc:`../examples/scripts/temp_frame_xml`
* :doc:`../examples/skills/bound_example_xml`
* :doc:`../examples/skills/spherical_velocity_xml`
