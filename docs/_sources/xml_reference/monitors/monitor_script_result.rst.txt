=====================
monitor_script_result
=====================

Triggers when a script returns a certain result.

Defined at line 128 of file :doc:`monitors/basic.xml <../model_files/pitasc_library/monitors/basic_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   logic

  | **Prototypes**
  |   monitor, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **script** : parameter:script
  |  The script to watch

  | **possible_results** : csv:string
  |  The possible results that can be returned by the script

  | **events** : csv:string
  |  The respective events that are fired, in the order according to the possible results

**Hidden** parameters:

  | **event** : string
  |  Primary event that is triggered by the monitor

Examples
========
No examples found that make use of **monitor_script_result**