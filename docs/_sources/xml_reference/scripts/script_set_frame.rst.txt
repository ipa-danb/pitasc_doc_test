================
script_set_frame
================

Sets a new frame.

Defined at line 119 of file :doc:`scripts/geometry.xml <../model_files/pitasc_library/scripts/geometry_xml>` in package **pitasc_library**.

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
  |  Name of the frame to be set or created

  | **parent** : string
  |  Name of the parent frame to of 'frame'

  | **pose** : csv:float
  |  Pose of the new frame relative to 'parent'

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

  | **pose_type** : string
  |  Specifies how the rotation part of pose is given.
  |  **Default**: rpy

Examples
========
No examples found that make use of **script_set_frame**