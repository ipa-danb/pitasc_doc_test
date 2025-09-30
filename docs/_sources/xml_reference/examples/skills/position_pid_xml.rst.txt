================
position_pid.xml
================

This example application shows the usage of some force skills.
Move to a target, establishes a contact, pushes for some seconds,
keeps on pushing while moving in another direction (slide), returns to the initial target

Models used
-----------

* :doc:`../../monitors/monitor_duration`: lines 68, 107, 146, 186
* :doc:`../../scripts/script_measurement_publisher`: lines 75, 114, 153, 193
* :doc:`../../skills/skill_cartesian_tracking_pid`: lines 53, 92, 131, 171
* :doc:`../../skills/skill_lin`: lines 48, 87, 126, 165, 205
* :doc:`../../skills/skill_relative_ptp`: lines 44
* :doc:`../../skills/skill_sequence`: lines 36

File contents
-------------


.. literalinclude:: position_pid.xml
    :language: xml
    :linenos:
    :emphasize-lines: 193,131,68,75,205,146,87,153,92,36,165,107,171,44,48,114,53,186,126
