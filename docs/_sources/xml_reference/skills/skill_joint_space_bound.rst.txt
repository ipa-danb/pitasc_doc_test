=======================
skill_joint_space_bound
=======================

Keeps on tracking a joint configuration

Defined at line 8 of file :doc:`skills/skill_joint_space_bound.xml <../model_files/pitasc_library/skills/skill_joint_space_bound_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, position_controlled

  | **Prototypes**
  |   :doc:`skill_joint_space`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **joint_names** : csv:string
  |  Joint names of the target pose.

  | **upper_bound** : csv:float
  |  List of upper bound values respective to axes.
  |  **Default**: 3.14, 3.14, 3.14, 3.14, 3.14, 3.14

  | **lower_bound** : csv:float
  |  List of lower bound values respective to axes.
  |  **Default**: -3.14, -3.14, -3.14, -3.14, -3.14, -3.14

**Expert** parameters:

  | **skill_name** : string
  |  Name of this skill. Must be locally unique.

  | **tasks** : list:task
  |  Contains the task description(s).

  | **bounds** : list:bound
  |  Contains the bounds description(s).
  |  **Default**: odict_keys(['tracking_bound'])

  | **monitors** : list:monitor
  |  Contains the monitors of the skill that determine when the skill should terminate.

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

  | **scaler** : float
  |  Time constant restricting the movement, i.e.,  v_allowed <  (p_bound - p_current) / scalar
  |  **Default**: 1.0

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['base_to_eef'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========

**skill_joint_space_bound** is used in the following examples:

* :doc:`../examples/skills/bound_example_xml`
