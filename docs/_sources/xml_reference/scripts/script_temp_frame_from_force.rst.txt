============================
script_temp_frame_from_force
============================

Creates a temporary frame from the current force measurements.

The z axis points in the opposite direction of the measured force vector (the usual definition for force control with pitasc).
The frame's position and direction will be updated as long as the script is active.

Includes possibility to filter the input with a first order low pass.

Defined at line 173 of file :doc:`scripts/geometry.xml <../model_files/pitasc_library/scripts/geometry_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   frames

  | **Prototypes**
  |   :doc:`script_temp_frame`, script_kinematic_graph, script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **frame** : string
  |  Name of the frame to be created

  | **source** : string
  |  Name of the frame to be copied

**Basic** parameters:

  | **on_start** : bool
  |  Execute the script before or after the skill.
  |  **Default**: True

  | **tf_broadcast** : bool
  |  Broadcast the frame to TF?
  |  **Default**: False

  | **low_pass_filter_gain** : float
  |  First order low pass filter gain (exponential filter). Must be in interval [0:1]. 0 means taking only the previous value, 1 means taking only the new value.
  |  **Default**: 1.0

**Expert** parameters:

  | **parent** : string
  |  Name of the parent frame to of 'frame'

  | **wrench_driver** : dict
  |  Base type for all data sources.

**Hidden** parameters:

  | **kinematic_graph** : dict
  |  Graph of kinematic links

Examples
========

**script_temp_frame_from_force** is used in the following examples:

* :doc:`../examples/scripts/temp_frame_xml`
