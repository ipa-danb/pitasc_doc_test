==================
skill_parallel.xml
==================

This example application shows the usage of a skill_parallel.

2 idle_duration skills will be executed. skill_parallel only finishes
after the last skill_idle_duration is done. A third skill (skill_idle)
never fires "succeeded", but skill_parallel is not blocked by this.

Models used
-----------

* :doc:`../../skills/skill_idle`: lines 63
* :doc:`../../skills/skill_idle_duration`: lines 52, 57
* :doc:`../../skills/skill_lin`: lines 42, 71
* :doc:`../../skills/skill_parallel`: lines 47
* :doc:`../../skills/skill_sequence`: lines 33

File contents
-------------


.. literalinclude:: skill_parallel.xml
    :language: xml
    :linenos:
    :emphasize-lines: 33,52,71,57,42,47,63
