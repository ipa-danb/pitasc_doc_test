=================
bound_example.xml
=================

This example application shows the usage of boundaries with the optimizer solver.
i.e.,
inequality constraints in cartesian and joint space
, weighted combination of conflicting
skill objectives

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 86
* :doc:`../../skills/skill_cartesian_bound`: lines 71, 118
* :doc:`../../skills/skill_concurrency`: lines 60, 97
* :doc:`../../skills/skill_joint_space_bound`: lines 125
* :doc:`../../skills/skill_lin`: lines 41, 47, 54, 62, 93
* :doc:`../../skills/skill_lin_trajectory`: lines 99
* :doc:`../../skills/skill_sequence`: lines 38

File contents
-------------


.. literalinclude:: bound_example.xml
    :language: xml
    :linenos:
    :emphasize-lines: 97,99,38,71,41,47,125,86,118,54,60,93,62
