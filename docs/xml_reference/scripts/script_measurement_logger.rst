=========================
script_measurement_logger
=========================

Logs internal measurements to a file.

Defined at line 62 of file :doc:`scripts/logging.xml <../model_files/pitasc_library/scripts/logging_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   logging

  | **Prototypes**
  |   script, object, dictionary, base, descriptive

Parameters
==========

**Required** parameters:

  | **provider** : list:data_source
  |  Data sources that provide the measurements for logging.

  | **file_name** : string
  |  Full path and name (incl. extension) of logging file.
  |  Non-existing directories are created.
  |  The following artifacts (enclosed by curly brackets) are dynamically resolved:
  |  '{rospkg (..)]}': full path to rospackge (..) (cf. roscd);
  |  '{time (..)}': current time with respective formating (..) (cf. std::strftime)

**Basic** parameters:

  | **filter** : csv:string
  |  Explicit names of the measurements to be logged.

  | **use_simple_filter_keys** : bool
  |  Allows to use filter keys without chain (e.g. 'x' instead of 'target_to_tool/x')
  |  **Default**: False

**Expert** parameters:

  | **buffer_length** : int
  |  Initial length of the preallocated buffer during logging.
  |  buffer_length = #samples * (#logged_coordinates + 1).
  |  May be extended on the fly.
  |  **Default**: 512

Examples
========

**script_measurement_logger** is used in the following examples:

* :doc:`../examples/scripts/logging_xml`
* :doc:`../examples/skills/lin_trajectory_xml`
* :doc:`../examples/skills/ptp_trajectory_xml`
