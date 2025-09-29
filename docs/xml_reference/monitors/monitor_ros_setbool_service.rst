===========================
monitor_ros_setbool_service
===========================

Triggers when a ROS SetBool service is called

Defined at line 90 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

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

**monitor_ros_setbool_service** is used in the following examples:

* :doc:`../examples/scripts/io_xml`
