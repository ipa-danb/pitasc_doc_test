============================
How to create a custom skill
============================

This guide explains how to create a simple custom skill that avoids the implementation of collections, loops, tasks and bounds by inheriting them from an already created skill.

.. For a more comprehensive look at how to create skills that use those, look at the follow-up how to...: ____

First, you have to create the file XML containing the skill. Good practice is to save custom skills in a separate ros package. Save your skill file in the ``/skills`` directory of your package and use the following naming convention
``skill_[skil_name].xml``.

.. code-block:: text

    package_name
    ├── examples
    ├── skills
    |   └── skill_[skill_name].xml    <-- Your skill_file
    └── ...

To create a simple skill, you need to first include everything that is part of your skill, e.g., skills, monitors, scripts, etc. Add the include statement at the start of the ``<models>`` tag with the following syntax.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="package_name" file="path/skill_[skill_name].xml"/>
            ...

.. Comment to get indent after code-block
..

    .. warning::

        Don't include xml-files that include the new skill itself. Otherwise you get an error message due to circular including.

The skill gets added right after the include statements in the ``<models>``. For this, use the ``<type>`` tag so that you can edit the metadata easily.

.. code-block:: xml
    :emphasize-lines: 1

    <type id="skill_[skill_name]" prototype="{base skill}">
        <!-- skill body -->
    </type>

.. Comment to get indent after code-block
..

    The ``id``, i.e., the skill name, should be unique and descriptive.

    The attribute ``prototype`` refers to the base skill, which is the basis of the new skill. If you want to create a skill that is a simple extension of another skill, this would be the prototype. An example of this would be the skill ``skill_idle_duration``, which has the prototype ``skill_idle`` and only attaches a ``monitor_duration`` monitor. If you want to create a more complex skill that includes multiple skills, the prototype must be a composition skill like, e.g., ``skill_concurrency``. An example of this would be the skill ``skill_guarded_approach``.

Set the metadata inside the ``<meta>`` tag of the skill.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 4,5,6

    ...
    <models>
    <meta>
        <member id="description"> {Description} </member>
        <member id="categories"> {category_1, category_2, ...} </member>
        <member id="visibility"> {choose required, basic, expert or hidden} </member>
    </meta>
    ...

.. Comment to get indent after code-block
..

    The parameter ``description`` contains a description. Describe the skill in as much detail as needed to understand the skill completely. This description can be used to create the automatically generated documentation.

    The parameter ``categories`` should include the categories of the parent skill and the categories of sub-skills. An exception to this is the internal category of base-skills. The category has no special meaning, but can help to sort the skills, e.g., in a documentation or a GUI. Examples for categories are the entries of :doc:`../../../xml_reference/skills/index`.

    The parameter ``visibility`` determines how a skill is shown inside the documentation. It can be set to required, basic, expert and hidden. In most cases, basic visibility should be used.

Inside the ``<data>`` tag, every component of the skill like parameters, sub-skills, etc are placed.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 4

    ...
    </meta>
    <data>
        <!-- skill components and implementation -->
    </data>

For an example of a very basic custom skill, see the example in the :doc:`../../fundamentals/skill` fundamentals.

The following guides explain how to add and use each type of component.

    | :doc:`How_to_add_a_parameter_to_a_skill_monitor_etc`
    | :doc:`../beginner/How_to_attach_a_monitor_to_a_skill`
    | :doc:`../beginner/How_to_attach_a_script_to_a_skill`







