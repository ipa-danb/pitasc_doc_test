============================
script_external_topic_logger
============================

Logs values from a ROS topic to a file.

Defined at line 65 of file :doc:`ros/ros_scripts.xml <../model_files/pitasc_library/ros/ros_scripts_xml>` in package **pitasc_library**.

Meta data
=========

  | **Categories**
  |   publisher

  | **Prototypes**
  |   :doc:`script_topic_logger`, script, object, dictionary, base, descriptive

Parameters
==========

**Hidden** parameters:

  | **topic** : string
  |  The ros topic to listen on

  | **fields** : list:string_parameter
  |  The Field in the topic to be logged. Syntax is comparable to 'rostopic echo': Lists with [], subitems with . (dot).
  |  
  |  Examples: "wrench.force", "wrench.force.x", "list[0]"

  | **package** : string
  |  A rospackage in the workspace to place the file in. Leave empty if absolute path is wanted.

  | **folder** : string
  |  An additional folder within the rospackage path. Creates folder if not existing.

  | **file_name** : string
  |  The name of the file to log the data into.
  |  
  |  Accepts subsequent folders, "~" for home (if package=="") and the following special artefacts:
  |  "{number}" -> starts at 0 and increases by one every time the logger is reentered within an application (e.g. application starts and stops logger in a loop);
  |  "{timestamp%Y-%m-%d_%H-%M-%S}" -> Is replaced by the timestamp at starting with the given structure.
  |  Examples: "{timestamp%Y-%m-%d}/{timestamp%H-%M-%S}_iteration_{number}.log" -> 2020-06-06/13-40-31_iteration_0.log

  | **file_mode** : string
  |  File creation flag:
  |  
  |  a  : if file already exists, new data will be appended,
  |  w  : new data will overwrite and replace already existing data,
  |  w+ : if file already exists, a new file will be created with additional surfix
  |  **Default**: w+

  | **name** : string
  |  Name of the external node to be created.

Examples
========
No examples found that make use of **script_external_topic_logger**