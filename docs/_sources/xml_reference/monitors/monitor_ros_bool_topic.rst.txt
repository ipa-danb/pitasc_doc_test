======================
monitor_ros_bool_topic
======================

Triggers when a ROS bool topic has a desired value

Defined at line 220 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   monitor_ros_topic_with_operator, monitor_ros_topic, monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **topic** : string
  |  Name of the topic to subscribe

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **namespace** : string
  |  Namespace of the topic to subscribe

  | **operator** : string
  |  Operator name (e.g. less, absolute_greater, greater_equal, absolute_less_equal,...)
  |  **Default**: equal

  | **value** : bool
  |  The desired value
  |  **Default**: True

Examples
========

**monitor_ros_bool_topic** is used in the following examples:

* :doc:`../examples/monitors/io_xml`
