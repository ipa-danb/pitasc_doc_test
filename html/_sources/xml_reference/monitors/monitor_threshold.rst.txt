=================
monitor_threshold
=================

Triggers when a measurement exceeds a certain threshold.

Defined at line 56 of file :doc:`monitors/measurements.xml <../model_files/pitasc_library/monitors/measurements_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   measurements

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **provider** : parameter:data_source
  |  Data source for which to check the outputs.

  | **coordinates** : csv:string
  |  Coordinate of the value to be checked

  | **prefix** : string
  |  Prefix for the coordinates

  | **operator** : string
  |  Defines if the measurements should be lower or greater than the thresholds.

  | **thresholds** : csv:float
  |  Threshold values

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **multi_coordinates_handling** : string
  |  Behavior for applying the thresholds to multiple coordinates.
  |  **Default**: single_element

  | **samples** : int
  |  Number of consecutive samples that need to meet the threshold condition before the monitor fires
  |  **Default**: 1

Examples
========

**monitor_threshold** is used in the following examples:

* :doc:`../examples/monitors/measurements_xml`
* :doc:`../examples/monitors/multiple_events_in_same_skill_xml`
* :doc:`../examples/scripts/temp_frame_xml`
* :doc:`../examples/skills/spherical_velocity_xml`
