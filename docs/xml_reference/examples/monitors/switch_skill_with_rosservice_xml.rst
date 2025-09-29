================================
switch_skill_with_rosservice.xml
================================

This example shows how to switch skills on runtime using an external trigger, namely a ros service.
Once you reached skill1, you can switch between skill1 and skill2 by calling the rosservice specified in the change_skill_monitor.
From terminal: `rosservice call /switch_skill "event: 'change_to_skill2'" ` (resp. `change_to_skill1` to switch back)

Models used
-----------

* :doc:`../../monitors/monitor_ros_fireevent_service`: lines 40
* :doc:`../../skills/skill_idle`: lines 61, 73
* :doc:`../../skills/skill_lin`: lines 48
* :doc:`../../skills/skill_statechart`: lines 35

File contents
-------------


.. literalinclude:: switch_skill_with_rosservice.xml
    :language: xml
    :linenos:
    :emphasize-lines: 35,40,73,48,61
