======================
script_call_empty_srvs
======================

Calls a srvs with type 'std_msgs/Empty'.

Defined at line 95 of file :doc:`scripts/io.xml <../model_files/pitasc_library/scripts/io_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   io

  | **Prototypes**
  |   script_service_caller, script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **service_name** : string
  |  Name of the service to be called

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

Examples
========

**script_call_empty_srvs** is used in the following examples:

* :doc:`../examples/beginner/rosservice_calls_xml`
* :doc:`../examples/scripts/io_xml`
