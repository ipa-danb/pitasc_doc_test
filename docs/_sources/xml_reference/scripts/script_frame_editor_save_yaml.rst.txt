=============================
script_frame_editor_save_yaml
=============================

Saves YAML with frame editor.

Defined at line 197 of file :doc:`frame_editor/frame_editor.xml <../model_files/pitasc_library/frame_editor/frame_editor_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   frames

  | **Prototypes**
  |   script_service_caller, script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **service_name** : string
  |  Name of the service to be called
  |  **Default**: /frame_editor/save_yaml

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

  | **filename** : string
  |  Name of the file to be saved

Examples
========
No examples found that make use of **script_frame_editor_save_yaml**