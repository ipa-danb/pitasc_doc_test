=========================
monitor_execution_counter
=========================

Triggers after a certain number of executions of the parent skill. Can trigger a **reject_event** if the number of exections is not reached yet.

Defined at line 67 of file :doc:`monitors/basic.xml <../model_files/pitasc_library/monitors/basic_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   logic

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **count** : int
  |  Number of executions before triggering

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **reject_event** : string
  |  The event to be triggered if count **is not** reached.
  |  **Default**: preempted

  | **fire_on_reject** : bool
  |  If true, the **reject_event** is triggered if the **count** is not reached yet.
  |  **Default**: False

Examples
========

**monitor_execution_counter** is used in the following examples:

* :doc:`../examples/beginner/simple_count_xml`
