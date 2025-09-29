================
monitor_distance
================

Triggers when each frame's coordinate relative to a reference frame exceeds a certain threshold.

Every coordinate is handled individually. Triggers when true for every coordinate.

Defined at line 40 of file :doc:`monitors/geometry.xml <../model_files/pitasc_library/monitors/geometry_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   geometry

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **reference_frame** : string
  |  Static frame from which the moving frame is observed (e.g. world).

  | **frame** : string
  |  Moving frame

  | **coordinates** : csv:string
  |  Observed axes.

  | **distances** : csv:float
  |  Distances threshold (m or rad). Aligned to the `distance_coordinates` member.

  | **operator** : string
  |  Operator name (e.g. less, absolute_greater, greater_equal, absolute_less_equal,...)

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **target_offsets** : csv:float
  |  Offsets to the target. There must be as many values as there are `coordinates`. If no value is given, 0 is used for all coordinates.

**Hidden** parameters:

  | **distance_coordinates** : csv:string
  |  Possible axes names that can be given in the member `coordinates`. The given `distances` are aligned to the axes given here.

  | **kinematic_graph** : dict
  |  Graph of kinematic links

Examples
========

**monitor_distance** is used in the following examples:

* :doc:`../examples/monitors/geometry_xml`
