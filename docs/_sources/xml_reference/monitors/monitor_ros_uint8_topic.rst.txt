=======================
monitor_ros_uint8_topic
=======================

Triggers when a ROS uint8 topic has a desired value.

Defined at line 302 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   :doc:`monitor_ros_int8_topic`, monitor_ros_topic_with_operator, monitor_ros_topic, monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **topic** : string
  |  Name of the topic to subscribe

  | **value** : int
  |  The desired value

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **namespace** : string
  |  Namespace of the topic to subscribe

  | **operator** : string
  |  Operator name (e.g. less, absolute_greater, greater_equal, absolute_less_equal,...)
  |  **Default**: equal

Examples
========
No examples found that make use of **monitor_ros_uint8_topic**