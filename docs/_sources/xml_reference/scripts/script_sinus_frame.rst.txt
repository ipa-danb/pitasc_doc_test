==================
script_sinus_frame
==================

Creates a temporary frame that lives as long as the parent skill is active. The frame moves in the given coordinate with a sinus

Defined at line 208 of file :doc:`scripts/geometry.xml <../model_files/pitasc_library/scripts/geometry_xml>` in package **pitasc_library**.

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

  | **parent** : string
  |  Name of the parent frame to of 'frame'

  | **coordinate** : string
  |  Coordinate that will be updated by a sine.

  | **amplitude** : float
  |  Amplitude of the sine.

  | **period** : float
  |  Period of the sine in [s].

**Basic** parameters:

  | **on_start** : bool
  |  Execute the script before or after the skill.
  |  **Default**: True

  | **tf_broadcast** : bool
  |  Broadcast the frame to TF?
  |  **Default**: False

**Hidden** parameters:

  | **kinematic_graph** : dict
  |  Graph of kinematic links

Examples
========

**script_sinus_frame** is used in the following examples:

* :doc:`../examples/scripts/temp_frame_xml`
