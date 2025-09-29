=================================
multiple_events_in_same_skill.xml
=================================

This example checks if a certain bug happens during event processing.

skill_guarded_approach contains 2 monitors that fire at the same time. In older versions,
this led to a transition to skill_lin ("back"), followed immediately by a transition
exiting the parent skill_sequence. This was due to a bug that checks monitors even after
their skill is already finished.

Models used
-----------

* :doc:`../../monitors/monitor_threshold`: lines 61
* :doc:`../../scripts/script_measurement_publisher`: lines 85
* :doc:`../../skills/skill_guarded_approach`: lines 53
* :doc:`../../skills/skill_idle_duration`: lines 81
* :doc:`../../skills/skill_lin`: lines 47, 72
* :doc:`../../skills/skill_sequence`: lines 39

File contents
-------------


.. literalinclude:: multiple_events_in_same_skill.xml
    :language: xml
    :linenos:
    :emphasize-lines: 81,53,85,39,72,61,47
