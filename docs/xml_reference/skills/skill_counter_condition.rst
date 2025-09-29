=======================
skill_counter_condition
=======================

Branches after a certain number of iterations

Defined at line 42 of file :doc:`skills/skill_idle_duration.xml <../model_files/pitasc_library/skills/skill_idle_duration_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, logic

  | **Prototypes**
  |   :doc:`skill_idle`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **count** : int
  |  Number of executions before triggering

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **repeat_target** : string
  |  Name of Target skill when condition is NOT reached

  | **condition_target** : string
  |  Name of Target skill when condition is reached
  |  **Default**: succeeded

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
  |  **Default**: odict_keys(['monitor_execution_counter'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.
  |  **Default**: odict_keys(['transition', 'transition_no0'])

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

Examples
========

**skill_counter_condition** is used in the following examples:

* :doc:`../examples/beginner/simple_count_xml`
* :doc:`../examples/monitors/sync_xml`
