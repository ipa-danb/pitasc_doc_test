===============
skill_log_force
===============

Logs a force/torque in a desired frame into a file

Defined at line 77 of file :doc:`skills/logging/skill_logging.xml <../model_files/pitasc_library/skills/logging/skill_logging_xml>` in package **pitasc_library**.

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
  |  Frame defining the desired position and axes for measuring force and torque

  | **file_name** : string
  |  Full path and name (incl. extension) of logging file.
  |  Non-existing directories are created.
  |  The following artifacts (enclosed by curly brackets) are dynamically resolved:
  |  '{rospkg (..)]}': full path to rospackge (..) (cf. roscd);
  |  '{time (..)}': current time with respective formating (..) (cf. std::strftime)

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **filter** : csv:string
  |  Explicit names of the measurements to be logged.

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
  |  **Default**: odict_keys(['script_measurement_logger'])

  | **force_sensor** : dict
  |  Force sensor that provides the wrench measurement.

  | **buffer_length** : int
  |  Initial length of the preallocated buffer during logging.
  |  buffer_length = #samples * (#logged_coordinates + 1).
  |  May be extended on the fly.
  |  **Default**: 512

**Hidden** parameters:

  | **collections** : list:collection
  |  Contains the kinematic chains of the skill (feature, robot, object chains).
  |  **Default**: odict_keys(['force_chain', 'object_chains'])

  | **loops** : list:kinematic_loop
  |  Contains the kinematic loop(s) that define the task to be solved.
  |  **Default**: odict_keys(['kinematic_loop'])

Examples
========

**skill_log_force** is used in the following examples:

* :doc:`../examples/scripts/logging_xml`
