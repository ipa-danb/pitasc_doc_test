======
pitasc
======
.. toctree::
    :hidden:
    :maxdepth: 1

*pitasc* is a robot control software mainly intended for force-controlled assembly using collaborative and industrial robots.
It has been utilized to solve numerous real-world applications. Some notable examples are the
`assembly of plastic components <https://www.youtube.com/watch?v=s0nBJR_MGwM>`_ as well as
`riveting, screwing and clipping <https://www.youtube.com/watch?v=1_VV98WQyMI>`_ applications.
*pitasc* also allows for `rapid reconfigurability <https://www.youtube.com/watch?v=XGdiYxBxXGk>`_ of flexible robot cells and the
coordinated control of two robot arms, e.g. for the `automated wiring of electrical cabinets <https://www.youtube.com/watch?v=xXR2FxPVqa4>`_.

*pitasc* follows a *skill*-based programming approach, i.e. robot programs are not programmed in a certain, possibly vendor-specific, programming language.
Instead, the developer arranges and parameterizes so called *skills*. *Skills* can either involve simple commands like LIN and PTP movements or
they can model more complex behaviour, possibly consisting of concurrent position and force control in different task space dimensions.
Real-world applications like the examples above usually necessitate these more sophisticated *skills*.



.. toctree::
    :maxdepth: 2
    :caption: User guide
    :hidden:

   user_guide/installation.rst
   user_guide/getting_started.rst
   user_guide/fundamentals/index.rst
   user_guide/how-to/index.rst



.. toctree::
    :maxdepth:1
    :hidden:

    user_guide/setup_robots



.. toctree::
   :maxdepth: 1
   :caption: XML Reference
   :hidden:

   xml_reference/skills/index.rst
   xml_reference/monitors/index.rst
   xml_reference/scripts/index.rst
   xml_reference/examples/index.rst



.. toctree::
   :maxdepth: 1
   :caption: API Reference
   :hidden:

   api_reference/python/index.rst

.. toctree::
   :maxdepth: 1
   :caption: Appendix
   :hidden:

   About <https://www.pitasc.fraunhofer.de/en.html>
   Contact <https://www.pitasc.fraunhofer.de/en/contact.html>
