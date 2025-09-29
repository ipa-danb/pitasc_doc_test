==============
skill_parallel
==============

Hierarchy of skills which are executed simultaneously. Ends with 'succeeded' only if **all** subskills triggered 'succeeded'.

If a subskill cannot finish with 'succeeded', it does not block the skill_parallel, except when there is no subskill that can trigger 'succeeded'.

As soon as one skill finishes, this skill drops out of the control hierarchy. **This means that the control hierarchy gets updated, resulting in a potentially fundamentally different robot behavior (due to the projection).**

Defined at line 228 of file :doc:`models/coordination.xml <../model_files/pitasc_library/models/coordination_xml>` in package **pitasc_library**.

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

**skill_parallel** is used in the following examples:

* :doc:`../examples/beginner/skill_parallel_xml`
* :doc:`../examples/dual_robot/bounds_dual_robot_xml`
* :doc:`../examples/dual_robot/dual_robot_forces_xml`
* :doc:`../examples/skills/forces_pid_xml`
