==================
ptp_trajectory.xml
==================

This example application shows how to run a ptp trajectory through several joint states with blending.

A UR5 moves to start position, then he performs the trajectory. Then, he does it again with higher velocity. Then the application terminates.

Models used
-----------

* :doc:`../../scripts/script_measurement_logger`: lines 77, 82
* :doc:`../../skills/skill_lin`: lines 50, 91
* :doc:`../../skills/skill_ptp_trajectory`: lines 56, 97
* :doc:`../../skills/skill_sequence`: lines 41

File contents
-------------


.. literalinclude:: ptp_trajectory.xml
    :language: xml
    :linenos:
    :emphasize-lines: 97,82,50,56,41,91,77
