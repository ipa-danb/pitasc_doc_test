======================
forces_feedforward.xml
======================

This example application shows the usage of a force skill with a feed-forward velocity.
The robot moves in z direction with a fixed velocity and controls the reaction force in the same direction additionally,

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 67
* :doc:`../../skills/skill_apply_force`: lines 55
* :doc:`../../skills/skill_concurrency`: lines 53
* :doc:`../../skills/skill_hold_pose`: lines 62
* :doc:`../../skills/skill_lin`: lines 47
* :doc:`../../skills/skill_relative_ptp`: lines 43
* :doc:`../../skills/skill_sequence`: lines 35

File contents
-------------


.. literalinclude:: forces_feedforward.xml
    :language: xml
    :linenos:
    :emphasize-lines: 67,35,53,55,43,62,47
