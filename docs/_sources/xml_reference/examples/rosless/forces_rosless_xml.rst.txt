==================
forces_rosless.xml
==================

This example application shows the usage of some force skills.
Move to a target, establishes a contact, pushes for some seconds,
keeps on pushing while moving in another direction (slide), returns to the initial target

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 83, 130, 175
* :doc:`../../skills/skill_guarded_approach`: lines 63
* :doc:`../../skills/skill_guarded_lin`: lines 144
* :doc:`../../skills/skill_guarded_slide`: lines 114
* :doc:`../../skills/skill_insert`: lines 161
* :doc:`../../skills/skill_lin`: lines 57, 138, 190
* :doc:`../../skills/skill_push`: lines 73
* :doc:`../../skills/skill_push_duration`: lines 89
* :doc:`../../skills/skill_push_settle`: lines 100
* :doc:`../../skills/skill_relative_ptp`: lines 53
* :doc:`../../skills/skill_sequence`: lines 45

File contents
-------------


.. literalinclude:: forces_rosless.xml
    :language: xml
    :linenos:
    :emphasize-lines: 89,161,130,100,73,138,45,175,144,114,83,53,57,190,63
