==============================
monitor_ros_fireevent_rostopic
==============================

Monitor which fires events according to the values on rostopic input.

Defined at line 139 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **topic** : string
  |  Name of the topic to subscribe

  | **values** : list:value_event_pair
  |  The desired values and corresponding events. Use the value_event_pair type.

  | **type** : string
  |  The desired type

**Basic** parameters:

  | **namespace** : string
  |  Namespace of the topic to subscribe

**Hidden** parameters:

  | **event** : string
  |  Unused, since 'values' contains the event names

Examples
========

**monitor_ros_fireevent_rostopic** is used in the following examples:

* :doc:`../examples/monitors/io_xml`
