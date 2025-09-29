==============
temp_frame.xml
==============

This example application shows the usage of the script_temp_frame_from_force. This is helpful for example when you do not know the orientation of a surface, but want to appply forces perpendicular to it.

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 117, 137
* :doc:`../../monitors/monitor_threshold`: lines 57, 86
* :doc:`../../scripts/script_sinus_frame`: lines 145
* :doc:`../../scripts/script_temp_frame_from_force`: lines 77
* :doc:`../../skills/skill_cartesian_tracking`: lines 132
* :doc:`../../skills/skill_concurrency`: lines 130
* :doc:`../../skills/skill_guarded_slide`: lines 101
* :doc:`../../skills/skill_lin`: lines 42, 124
* :doc:`../../skills/skill_push`: lines 49, 69
* :doc:`../../skills/skill_sequence`: lines 34

File contents
-------------


.. literalinclude:: temp_frame.xml
    :language: xml
    :linenos:
    :emphasize-lines: 130,34,132,101,69,137,42,77,145,49,117,86,57,124
