=======================
skill_cylindrical_helix
=======================

A skill that performs a cylindrical helix around z axis of the specified pivot_frame

Defined at line 11 of file :doc:`skills/cylindrical/skill_cylindrical_helix.xml <../model_files/pitasc_library/skills/cylindrical/skill_cylindrical_helix_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   single_robot, velocity_controlled

  | **Prototypes**
  |   :doc:`skill_sequence`, skill_single_robot, skill, object, dictionary, base, descriptive

Parameters
==========

**Basic** parameters:

  | **robot** : dict
  |  Robot that is controlled by the skill (only needs to be set at the application level).

  | **tool_frame** : string
  |  The used tool frame.
  |  **Default**: tool

  | **pivot_frame** : string
  |  The pivot point (i.e. tip of the cone).
  |  **Default**: pivot_point

  | **radius** : float
  |  Distance from the desired start point to the origin of pivot_frame [m].
  |  **Default**: 0.05

  | **height** : csv:float
  |  Distance from the desired end point to the origin of pivot_frame [m]. Only one value allowed.
  |  **Default**: 0.2

  | **start_phi** : float
  |  Initial value of angle phi (in x-y-plane of pivot_frame) [rad].
  |  **Default**: False

  | **helix_linear_velocity** : float
  |  The speed of the motion in radial direction
  |  **Default**: 0.005

  | **helix_angular_velocity** : float
  |  The speed of the rotation movement.
  |  **Default**: 0.5

  | **tool_direction** : list:float_parameter
  |  The rpy tool orientation (a,b,c) in [rad]
  |  **Default**: odict_keys(['a', 'b', 'c'])

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

  | **initial_skill** : string
  |  First skill to run.

  | **skills** : list:skill
  |  Sub-skills that are executed in sequence.
  |  **Default**: odict_keys(['skill_cylindrical_positioning', 'skill_concurrency'])

**Hidden** parameters:

  | **des_velocities** : list:float_parameter
  |  Defines the helix velocities
  |  **Default**: odict_keys(['helix_angular_velocity', 'helix_linear_velocity'])

  | **start_offsets** : list:float_parameter
  |  Defines the helix - r, phi, z, a, b, c
  |  **Default**: odict_keys(['radius', 'start_phi', 'float_parameter', 'tool_direction-a', 'tool_direction-b', 'tool_direction-c'])

  | **constant_offsets** : list:float_parameter
  |  Defines the helix - constant offsets (r, a, b, c)
  |  **Default**: odict_keys(['radius', 'tool_direction-a', 'tool_direction-b', 'tool_direction-c'])

Examples
========

**skill_cylindrical_helix** is used in the following examples:

* :doc:`../examples/skills/cylindrical_helix_xml`
