====================
rosservice_calls.xml
====================

This example application shows a minimal project.

A UR5 idles for 3 seconds. Then the application terminates.

Models used
-----------

* :doc:`../../scripts/script_call_empty_srvs`: lines 54, 77
* :doc:`../../scripts/script_call_setbool_srvs`: lines 61, 86
* :doc:`../../scripts/script_call_trigger_srvs`: lines 57, 81
* :doc:`../../skills/skill_hold_duration`: lines 50, 73
* :doc:`../../skills/skill_ptp`: lines 45, 69
* :doc:`../../skills/skill_sequence`: lines 38

File contents
-------------


.. literalinclude:: rosservice_calls.xml
    :language: xml
    :linenos:
    :emphasize-lines: 69,38,73,77,45,81,50,86,54,57,61
