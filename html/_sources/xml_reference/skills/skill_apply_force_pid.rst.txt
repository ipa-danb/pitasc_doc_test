=====================
skill_apply_force_pid
=====================

Applies a force in the direction of a frame

Defined at line 9 of file :doc:`skills/skill_apply_force_pid.xml <../model_files/pitasc_library/skills/skill_apply_force_pid_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, force_controlled

  | **Prototypes**
  |   :doc:`skill_force`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **force_frame** : string
  |  Frame describing the force coordinates

  | **axes** : csv:string
  |  List of axes.

  | **target_forces** : csv:float
  |  Forces and torques to be applied. Must be the same
  |  number of values as for 'axes'.

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

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

  | **tasks** : list:task
  |  Contains the task description(s).
  |  **Default**: odict_keys(['apply_force'])

  | **K** : float
  |  The gain K of the controller
  |  **Default**: 0.001

  | **Tn** : float
  |  The constant Tn impacts the systems inversely, so higher Tn means slower impact
  |  **Default**: False

  | **Tv** : float
  |  The constant Tv impacts the system directly,(its a part of D component), so higher Tv means faster response
  |  **Default**: False

  | **Tp** : float
  |  Compliance [m/(s*N)]
  |  **Default**: 0.001

  | **u_i_limit** : float
  |  The output limit of the i part of the controller
  |  **Default**: False

  | **I_flag** : bool
  |  Parameter to switch integral part on/off
  |  **Default**: False

  | **D_flag** : bool
  |  Parameter to switch derivative part on/off
  |  **Default**: False

Examples
========

**skill_apply_force_pid** is used in the following examples:

* :doc:`../examples/skills/forces_pid_xml`
