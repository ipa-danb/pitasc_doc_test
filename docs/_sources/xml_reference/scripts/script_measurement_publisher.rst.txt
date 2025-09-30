============================
script_measurement_publisher
============================

Publishes measurement values.

Defined at line 25 of file :doc:`scripts/logging.xml <../model_files/pitasc_library/scripts/logging_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   publisher

  | **Prototypes**
  |   script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **provider** : parameter:data_source
  |  Data source that provides the measurements to publish.

  | **coordinates** : csv:string
  |  Coordinates that should be published.

**Basic** parameters:

  | **topic** : string
  |  Topic name on which to publish.
  |  **Default**: measurements

Examples
========

**script_measurement_publisher** is used in the following examples:

* :doc:`../examples/monitors/multiple_events_in_same_skill_xml`
* :doc:`../examples/scripts/logging_xml`
* :doc:`../examples/skills/position_pid_xml`
