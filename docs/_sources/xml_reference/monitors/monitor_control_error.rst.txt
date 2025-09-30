=====================
monitor_control_error
=====================

Checks control_errors (desired vs. measured values)

Defined at line 7 of file :doc:`monitors/measurements.xml <../model_files/pitasc_library/monitors/measurements_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   measurements

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **controllers** : list:controller
  |  Controllers for which to check the control errors.

  | **coordinates** : csv:string
  |  Coordinates to be monitored

  | **prefix** : string
  |  Prefix for the coordinates

  | **thresholds** : csv:float
  |  Thresholds for the control errors

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **samples** : int
  |  Number of consecutive samples to be below the threshold before raising the event
  |  **Default**: 1

Examples
========
No examples found that make use of **monitor_control_error**