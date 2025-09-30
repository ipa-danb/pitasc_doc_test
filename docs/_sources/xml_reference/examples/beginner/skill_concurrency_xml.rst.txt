=====================
skill_concurrency.xml
=====================

This example application shows the usage of a skill hierarchy.

With a low priority, the robot tracks target1 ("my_tracker"). With a high
priority, the robot sequencially moves up and down along the z axis
("my_hierarchy"). After six seconds, the application terminates.

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 64, 78, 92, 111
* :doc:`../../skills/skill_cartesian_tracking`: lines 101
* :doc:`../../skills/skill_cartesian_velocity`: lines 57, 71, 85
* :doc:`../../skills/skill_concurrency`: lines 49
* :doc:`../../skills/skill_lin`: lines 42
* :doc:`../../skills/skill_sequence`: lines 33, 53

File contents
-------------


.. literalinclude:: skill_concurrency.xml
    :language: xml
    :linenos:
    :emphasize-lines: 64,33,101,71,42,78,111,49,85,53,57,92
