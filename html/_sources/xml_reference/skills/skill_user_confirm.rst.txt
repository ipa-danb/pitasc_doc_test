==================
skill_user_confirm
==================

Opens a dialog window to receive confirmation from the user.

Defined at line 9 of file :doc:`skills/skill_user_confirm.xml <../model_files/pitasc_library/skills/skill_user_confirm_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   user

  | **Prototypes**
  |   :doc:`skill_idle`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **title** : string
  |  The event to be triggered on success.
  |  **Default**: Confirmation required

  | **text** : string
  |  The event to be triggered on failure.
  |  **Default**: Proceed with application?

  | **ignore** : bool
  |  Parameter to ignore this skill and fire the (success) event immediately
  |  **Default**: False

  | **event** : string
  |  The event to be triggered on success.
  |  **Default**: succeeded

  | **reject_event** : string
  |  The event to be triggered on failure.
  |  **Default**: preempted

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
  |  **Default**: odict_keys(['monitor_user_confirm'])

  | **transitions** : list:transition
  |  Contains additional transitions to other states (skills), given an event name.

  | **scripts** : list:script
  |  Contains scripts that should be executed while the skill is active.

Examples
========

**skill_user_confirm** is used in the following examples:

* :doc:`../examples/monitors/user_confirm_xml`
