==========
forces.xml
==========

This example application shows the usage of some force skills.
Move to a target, establishes a contact, pushes for some seconds,
keeps on pushing while moving in another direction (slide), returns to the initial target

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 73, 120, 164
* :doc:`../../skills/skill_guarded_approach`: lines 54
* :doc:`../../skills/skill_guarded_lin`: lines 133
* :doc:`../../skills/skill_guarded_slide`: lines 104
* :doc:`../../skills/skill_insert`: lines 150
* :doc:`../../skills/skill_lin`: lines 48, 127, 179
* :doc:`../../skills/skill_push`: lines 63
* :doc:`../../skills/skill_push_duration`: lines 79
* :doc:`../../skills/skill_push_settle`: lines 90
* :doc:`../../skills/skill_relative_ptp`: lines 44
* :doc:`../../skills/skill_sequence`: lines 36

File contents
-------------


.. literalinclude:: forces.xml
    :language: xml
    :linenos:
    :emphasize-lines: 164,133,36,104,73,44,79,48,179,150,54,120,90,63,127
