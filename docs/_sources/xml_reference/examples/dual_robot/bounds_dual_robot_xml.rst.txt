=====================
bounds_dual_robot.xml
=====================

This example application shows the usage of 2 robots in the same app
(both sequentially and
concurrently).

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 76, 150
* :doc:`../../skills/skill_cartesian_bound`: lines 66, 119, 139
* :doc:`../../skills/skill_concurrency`: lines 59, 112, 131
* :doc:`../../skills/skill_lin`: lines 61, 83, 91, 98, 114, 133
* :doc:`../../skills/skill_parallel`: lines 108
* :doc:`../../skills/skill_sequence`: lines 50, 55

File contents
-------------


.. literalinclude:: bounds_dual_robot.xml
    :language: xml
    :linenos:
    :emphasize-lines: 66,131,98,133,91,139,76,108,112,114,83,50,55,150,119,59,61
