==========================
script_frame_editor_remove
==========================

Removes a frame from the frame_editor via ROS service.

Defined at line 71 of file :doc:`frame_editor/frame_editor.xml <../model_files/pitasc_library/frame_editor/frame_editor_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   frames

  | **Prototypes**
  |   script_frame_editor, script_service_caller, script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **service_name** : string
  |  Name of the service to be called
  |  **Default**: /frame_editor/remove_frame

**Basic** parameters:

  | **namespace** : string
  |  Namespace of the service to be called

  | **on_start** : bool
  |  If true, the script is executed when the parent skill starts
  |  **Default**: True

  | **blocking** : bool
  |  Decides if the ros service call blocks the pitasc cycle until the service returned. If set to false, on_start must be set to true.
  |  **Default**: True

  | **wait_for_service** : bool
  |  Wait until service becomes available
  |  **Default**: True

**Hidden** parameters:

  | **frame** : string
  |  Name of the frame to be removed

Examples
========
No examples found that make use of **script_frame_editor_remove**