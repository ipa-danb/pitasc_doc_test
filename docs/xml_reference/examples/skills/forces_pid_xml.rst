==============
forces_pid.xml
==============

This example application shows the usage of some force skills.
Move to a target, establishes a contact, pushes for some seconds,
keeps on pushing while moving in another direction (slide), returns to the initial target

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 82, 127, 170
* :doc:`../../skills/skill_apply_force_pid`: lines 56, 101, 144
* :doc:`../../skills/skill_hold_pose`: lines 75, 120, 163
* :doc:`../../skills/skill_lin`: lines 48, 92, 136, 179
* :doc:`../../skills/skill_parallel`: lines 53, 98, 141
* :doc:`../../skills/skill_relative_ptp`: lines 44
* :doc:`../../skills/skill_sequence`: lines 36

File contents
-------------


.. literalinclude:: forces_pid.xml
    :language: xml
    :linenos:
    :emphasize-lines: 136,75,141,144,82,56,92,98,163,36,101,170,44,48,179,53,120,127
