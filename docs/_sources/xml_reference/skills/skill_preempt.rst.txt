=============
skill_preempt
=============

Triggers a preempt event

Defined at line 97 of file :doc:`skills/skill_idle_duration.xml <../model_files/pitasc_library/skills/skill_idle_duration_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, logic

  | **Prototypes**
  |   :doc:`skill_idle_once`, :doc:`skill_idle_duration`, :doc:`skill_idle`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **duration** : float
  |  Skill duration in [s].
  |  **Default**: 0.001

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
  |  **Default**: odict_keys(['monitor_duration'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

Examples
========
No examples found that make use of **skill_preempt**