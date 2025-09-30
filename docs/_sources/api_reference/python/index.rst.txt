====================
Python API reference
====================

.. toctree::
    :hidden:
    :maxdepth: 1

Model access
------------

.. toctree::
    :hidden:
    :maxdepth: 2

    pitasc_model
    pitasc_model_interface
    pitasc_parameter_model
    pitasc_model_element

* :doc:`pitasc_model`
  : Contains functionality for creating and modifying pitasc models and loading existing models from XML.
* :doc:`pitasc_model_interface`
  : Convenience tools for accessing and modifying pitasc models more easily.
* :doc:`pitasc_parameter_model`
  : Contains functionality for creating and modifying pitasc model elements (used by :doc:`pitasc_model`).
* :doc:`pitasc_model_element`
  : Convenience tools for accessing and modifying pitasc model elements more easily (used by :doc:`pitasc_model_interface`).

Runtime access
--------------

.. toctree::
    :hidden:
    :maxdepth: 2

* :doc:`cppitasc_logging`
  : Logging functionality used by the pitasc runtime.
* :doc:`cppitasc_runtime`
  : Runtime access for executing pitasc applications and runtime data exchange.

.. toctree::
    :hidden:
    :maxdepth: 2

    cppitasc_logging
    cppitasc_runtime
