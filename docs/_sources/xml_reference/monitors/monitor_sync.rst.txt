============
monitor_sync
============

Contains other monitors and triggers when all sub-events match.

Defined at line 17 of file :doc:`monitors/basic.xml <../model_files/pitasc_library/monitors/basic_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   logic

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **monitors** : list:monitor
  |  Sub-monitors that need to be synced.

**Basic** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor
  |  **Default**: succeeded

  | **events** : csv:string
  |  Events that trigger the sync. If empty, **succeeded** is assumed for all sub monitors.

Examples
========

**monitor_sync** is used in the following examples:

* :doc:`../examples/monitors/sync_xml`
