=============
blacklist.xml
=============

This example application shows how blacklisted parameters work.
The skill_partial_velocity has an attribute 'referende_id' instead of 'reference_id', causing it to be empty.
The blacklist detects that and fires an error.

Models used
-----------

* :doc:`../../monitors/monitor_relative_distance`: lines 65
* :doc:`../../skills/skill_lin`: lines 50
* :doc:`../../skills/skill_partial_velocity`: lines 55
* :doc:`../../skills/skill_sequence`: lines 41

File contents
-------------


.. literalinclude:: blacklist.xml
    :language: xml
    :linenos:
    :emphasize-lines: 65,50,41,55
