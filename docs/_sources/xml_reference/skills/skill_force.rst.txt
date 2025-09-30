===========
skill_force
===========

Models a loop for force control

Defined at line 8 of file :doc:`skills/skill_force.xml <../model_files/pitasc_library/skills/skill_force_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, force_controlled

  | **Prototypes**
  |   skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **force_frame** : string
  |  Frame describing the force coordinates

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

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

  | **force_sensor** : dict
  |  Force sensor that provides the wrench measurement.

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['force_chain', 'object_chains'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========

**skill_force** is used in the following examples:

* :doc:`../examples/monitors/measurements_xml`
