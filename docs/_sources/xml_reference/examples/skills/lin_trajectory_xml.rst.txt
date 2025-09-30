==================
lin_trajectory.xml
==================

This example application shows how to run a linear trajectory through several waypoints with blending.

A UR5 moves to start position, then he performs the trajectory. Then, he does it again with higher velocity. Then the application terminates.

Models used
-----------

* :doc:`../../scripts/script_measurement_logger`: lines 93, 98
* :doc:`../../skills/skill_lin`: lines 50, 107
* :doc:`../../skills/skill_lin_trajectory`: lines 56, 113
* :doc:`../../skills/skill_sequence`: lines 41

File contents
-------------


.. literalinclude:: lin_trajectory.xml
    :language: xml
    :linenos:
    :emphasize-lines: 113,98,50,56,41,107,93
