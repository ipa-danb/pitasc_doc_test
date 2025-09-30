====================
monitor_frame_in_box
====================

Check whether a frame lies inside a bounding box.

Defined at line 177 of file :doc:`monitors/geometry.xml <../model_files/pitasc_library/monitors/geometry_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   geometry

  | **Prototypes**
  |   :doc:`monitor_distance`, monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **frame** : string
  |  Name of the frame to check.

  | **box_center_frame** : string
  |  Name of the frame in the center of the box.

  | **edge_length_xyz** : csv:float
  |  Size of the box in x, y and direction.

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **target_offsets** : csv:float
  |  Offsets to the target. There must be as many values as there are `coordinates`. If no value is given, 0 is used for all coordinates.

**Expert** parameters:

  | **coordinates** : csv:string
  |  Observed axes.
  |  **Default**: x, y, z

**Hidden** parameters:

  | **reference_frame** : string
  |  Static frame from which the moving frame is observed (e.g. world).

  | **distance_coordinates** : csv:string
  |  Possible axes names that can be given in the member `coordinates`. The given `distances` are aligned to the axes given here.
  |  **Default**: x, y, z

  | **distances** : csv:float
  |  Distances threshold (m or rad). Aligned to the `distance_coordinates` member.

  | **operator** : string
  |  Operator name (e.g. less, absolute_greater, greater_equal, absolute_less_equal,...)
  |  **Default**: absolute_less_equal

  | **kinematic_graph** : dict
  |  Graph of kinematic links

Examples
========

**monitor_frame_in_box** is used in the following examples:

* :doc:`../examples/monitors/geometry_xml`
