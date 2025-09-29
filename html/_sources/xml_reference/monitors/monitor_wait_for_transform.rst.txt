==========================
monitor_wait_for_transform
==========================

Triggers when a frame becomes available.

Defined at line 7 of file :doc:`monitors/geometry.xml <../model_files/pitasc_library/monitors/geometry_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   geometry

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **frame** : string
  |  Transform target to wait for.

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **parent_frame** : string
  |  Transform source frame to wait for.
  |  **Default**: world

**Hidden** parameters:

  | **kinematic_graph** : dict
  |  Graph of kinematic links

Examples
========
No examples found that make use of **monitor_wait_for_transform**