=================
script_temp_frame
=================

Creates a temporary frame that lives as long as the parent skill is active.

Defined at line 67 of file :doc:`scripts/geometry.xml <../model_files/pitasc_library/scripts/geometry_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   frames

  | **Prototypes**
  |   script_kinematic_graph, script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **frame** : string
  |  Name of the frame to be created

  | **source** : string
  |  Name of the frame to be copied

  | **parent** : string
  |  Name of the parent frame to of 'frame'

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
No examples found that make use of **script_temp_frame**