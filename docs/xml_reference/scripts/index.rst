=======
Scripts
=======

.. toctree::
    :hidden:
    :maxdepth: 1

frames
------

* :doc:`script_frame_editor_align`
  : Aligns a frame with another frame via frame editor ROS
* :doc:`script_frame_editor_copy`
  : Copies a frame via ROS service.
* :doc:`script_frame_editor_load_yaml`
  : Loads YAML with frame editor.
* :doc:`script_frame_editor_remove`
  : Removes a frame from the frame_editor via ROS service.
* :doc:`script_frame_editor_save_yaml`
  : Saves YAML with frame editor.
* :doc:`script_frame_editor_set`
  : Sets a new frame in the frame_editor via ROS service.
* :doc:`script_frame_editor_set_parent`
  : Set a new parent frame of a given frame via ROS service.
* :doc:`script_set_frame`
  : Sets a new frame.
* :doc:`script_set_frame_rotvec`
  : Sets a new frame (pose with rotation vector).
* :doc:`script_sinus_frame`
  : Creates a temporary frame that lives as long as the parent skill is active. The frame moves in the given coordinate with a sinus
* :doc:`script_temp_frame`
  : Creates a temporary frame that lives as long as the parent skill is active.
* :doc:`script_temp_frame_from_force`
  : Creates a temporary frame from the current force measurements.

.. toctree::
    :hidden:
    :maxdepth: 2

    script_frame_editor_align
    script_frame_editor_copy
    script_frame_editor_load_yaml
    script_frame_editor_remove
    script_frame_editor_save_yaml
    script_frame_editor_set
    script_frame_editor_set_parent
    script_set_frame
    script_set_frame_rotvec
    script_sinus_frame
    script_temp_frame
    script_temp_frame_from_force

io
--

* :doc:`script_call_empty_srvs`
  : Calls a srvs with type 'std_msgs/Empty'.
* :doc:`script_call_setbool_srvs`
  : Calls a srvs with type 'std_msgs/SetBool'.
* :doc:`script_call_trigger_srvs`
  : Calls a srvs with type 'std_msgs/Trigger'.

.. toctree::
    :hidden:
    :maxdepth: 2

    script_call_empty_srvs
    script_call_setbool_srvs
    script_call_trigger_srvs

logging
-------

* :doc:`script_error_logger`
  : Logs control_errors (desired vs. measured values)
* :doc:`script_measurement_logger`
  : Logs internal measurements to a file.

.. toctree::
    :hidden:
    :maxdepth: 2

    script_error_logger
    script_measurement_logger

publisher
---------

* :doc:`script_external_topic_logger`
  : Logs values from a ROS topic to a file.
* :doc:`script_measurement_publisher`
  : Publishes measurement values.
* :doc:`script_topic_logger`
  : Logs values from a ROS topic to a file.

.. toctree::
    :hidden:
    :maxdepth: 2

    script_external_topic_logger
    script_measurement_publisher
    script_topic_logger
