====================
monitor_user_confirm
====================

Opens a dialog window to receive confirmation from the user.

Defined at line 406 of file :doc:`monitors/io.xml <../model_files/pitasc_library/monitors/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **title** : string
  |  Title of the dialog window
  |  **Default**: Confirmation required

  | **text** : string
  |  Text of the dialog window (Question)
  |  **Default**: Proceed with application?

  | **ignore** : bool
  |  Parameter to skip the user confirm dialog and fire the (success) event immediately.
  |  **Default**: False

  | **reject_event** : string
  |  The event to be triggered on failure.
  |  **Default**: preempted

Examples
========

**monitor_user_confirm** is used in the following examples:

* :doc:`../examples/monitors/user_confirm_xml`
