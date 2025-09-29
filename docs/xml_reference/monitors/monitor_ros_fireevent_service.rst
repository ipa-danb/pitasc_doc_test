=============================
monitor_ros_fireevent_service
=============================

Fires an event with eventname given by service call

Defined at line 103 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   monitor_ros_service, monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **service_name** : string
  |  Name of the service to be provided

**Basic** parameters:

  | **namespace** : string
  |  Namespace of the service to be provided

**Hidden** parameters:

  | **event** : string
  |  Unused, the event name comes from the service call

Examples
========

**monitor_ros_fireevent_service** is used in the following examples:

* :doc:`../examples/monitors/switch_skill_with_rosservice_xml`
