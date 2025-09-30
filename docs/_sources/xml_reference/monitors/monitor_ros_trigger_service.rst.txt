===========================
monitor_ros_trigger_service
===========================

Triggers when a ROS Trigger service is called

Defined at line 77 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

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

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **namespace** : string
  |  Namespace of the service to be provided

Examples
========

**monitor_ros_trigger_service** is used in the following examples:

* :doc:`../examples/scripts/io_xml`
