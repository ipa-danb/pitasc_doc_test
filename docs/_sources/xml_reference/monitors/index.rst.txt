========
Monitors
========

.. toctree::
    :hidden:
    :maxdepth: 1

geometry
--------

* :doc:`monitor_distance`
  : Triggers when each frame's coordinate relative to a reference frame exceeds a certain threshold.
* :doc:`monitor_frame_in_box`
  : Check whether a frame lies inside a bounding box.
* :doc:`monitor_relative_distance`
  : Triggers when a frame moved a certain relative distance.
* :doc:`monitor_wait_for_transform`
  : Triggers when a frame becomes available.

.. toctree::
    :hidden:
    :maxdepth: 2

    monitor_distance
    monitor_frame_in_box
    monitor_relative_distance
    monitor_wait_for_transform

io
--

* :doc:`monitor_ros_bool_topic`
  : Triggers when a ROS bool topic has a desired value
* :doc:`monitor_ros_empty_service`
  : Triggers when a ROS Empty service is called
* :doc:`monitor_ros_fireevent_rostopic`
  : Monitor which fires events according to the values on rostopic input.
* :doc:`monitor_ros_fireevent_service`
  : Fires an event with eventname given by service call
* :doc:`monitor_ros_int16_topic`
  : Triggers when a ROS int16 topic has a desired value.
* :doc:`monitor_ros_int32_topic`
  : Triggers when a ROS int32 topic has a desired value.
* :doc:`monitor_ros_int64_topic`
  : Triggers when a ROS int64 topic has a desired value.
* :doc:`monitor_ros_int8_topic`
  : Triggers when a ROS int8 topic has a desired value.
* :doc:`monitor_ros_setbool_service`
  : Triggers when a ROS SetBool service is called
* :doc:`monitor_ros_trigger_service`
  : Triggers when a ROS Trigger service is called
* :doc:`monitor_ros_uint16_topic`
  : Triggers when a ROS uint16 topic has a desired value.
* :doc:`monitor_ros_uint32_topic`
  : Triggers when a ROS uint32 topic has a desired value.
* :doc:`monitor_ros_uint64_topic`
  : Triggers when a ROS uint64 topic has a desired value.
* :doc:`monitor_ros_uint8_topic`
  : Triggers when a ROS uint8 topic has a desired value.
* :doc:`monitor_user_confirm`
  : Opens a dialog window to receive confirmation from the user.

.. toctree::
    :hidden:
    :maxdepth: 2

    monitor_ros_bool_topic
    monitor_ros_empty_service
    monitor_ros_fireevent_rostopic
    monitor_ros_fireevent_service
    monitor_ros_int16_topic
    monitor_ros_int32_topic
    monitor_ros_int64_topic
    monitor_ros_int8_topic
    monitor_ros_setbool_service
    monitor_ros_trigger_service
    monitor_ros_uint16_topic
    monitor_ros_uint32_topic
    monitor_ros_uint64_topic
    monitor_ros_uint8_topic
    monitor_user_confirm

logic
-----

* :doc:`monitor_duration`
  : Triggers after a certain time.
* :doc:`monitor_execution_counter`
  : Triggers after a certain number of executions of the parent skill. Can trigger a **reject_event** if the number of exections is not reached yet.
* :doc:`monitor_script_result`
  : Triggers when a script returns a certain result.
* :doc:`monitor_sync`
  : Contains other monitors and triggers when all sub-events match.

.. toctree::
    :hidden:
    :maxdepth: 2

    monitor_duration
    monitor_execution_counter
    monitor_script_result
    monitor_sync

measurements
------------

* :doc:`monitor_control_error`
  : Checks control_errors (desired vs. measured values)
* :doc:`monitor_threshold`
  : Triggers when a measurement exceeds a certain threshold.

.. toctree::
    :hidden:
    :maxdepth: 2

    monitor_control_error
    monitor_threshold
