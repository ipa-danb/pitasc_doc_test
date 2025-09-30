==============================
script_frame_editor_set_parent
==============================

Set a new parent frame of a given frame via ROS service.

Defined at line 88 of file :doc:`frame_editor/frame_editor.xml <../model_files/pitasc_library/frame_editor/frame_editor_xml>` in package **pitasc_library**.

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
  |  **Default**: /frame_editor/set_parent

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
  |  Name of the frame to be created

  | **parent** : string
  |  Name of the parent frame

  | **keep_absolute** : bool
  |  If true, change the kin. tree, but not the position
  |  relative to 'world' or attach full transformation to parent frame

Examples
========
No examples found that make use of **script_frame_editor_set_parent**