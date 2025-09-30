===============
How to log data
===============

Sometimes, information about the execution of an application like position or force values is required, e.g., for documentation or debugging. Therefore, to provide a way to log data, pitasc has already implemented multiple scripts and skills. This How-To gives you an introduction to those logging skills and scripts. Note that the skills are designed to give a simpler interface to the logging scripts for common use-cases, i.e., if you want to log positions or forces, using the skills could be simpler compared to the scripts.

In the example :doc:`../../../xml_reference/examples/scripts/logging_xml`, you will find multiple examples of all
logging scripts and skills.

Scripts
-------

Scripts are attached to skills and run in parallel with them. See :doc:`How_to_attach_a_script_to_a_skill`.

script_measurement_logger
~~~~~~~~~~~~~~~~~~~~~~~~~

The script ``script_measurement_logger`` is one way to log data. It also functions as a basis for the other logging
scripts and skills.

.. code-block:: xml

    <scripts>
        <clone prototype="script_measurement_logger">
            <member id="provider" reference_id="move_skill.collections.target_to_tool.chains"/>
            <member id="file_name">{rospkg package_name}/path/{time %F_%H_%M_%S}_file_name.csv</member>
            <member id="use_simple_filter_keys">True</member>
            <member id="filter">z</member>
        </clone>
    </scripts>

The member parameter ``provider`` contains a list of the data sources that provide the measurement. Either
reference a list or add each data source separately, see
:doc:`How_to_set_the_value_of_a_parameter`. Viable data sources are:

    | - controllers
    | - kinematic_chains
    | - setpoint_generators
    | - drivers: (robot_drivers, wrench_drivers, wrench_transformer, driver_tf, cylindrical_driver,
        spherical_driver)


Some data sources like chains can not be referenced directly and need to be navigated to by using the ``.``
e.g. ``move_skill.collections.target_to_tool.chains``

The parameter ``file_name`` contains the full path and name of the log-file. Non-existing
directories are created. Use {} to dynamically change the path. The following artifacts are resolved

    | - {rospkg package_name}: Full path to package.
    | - {time %F_%H_%M_%S}: Current time formatted by using "std::strftime".

The parameter ``use_simple_filter_keys`` is a bool value if true, keys in the parameter filter can be shorted by omitting the chain (e.g. ‘x’ instead of ‘target_to_tool/x’).

The parameter ``filter`` contains the names of the measurements to be logged. If left empty, every measurement is logged.

The parameter ``buffer_length`` determines the initial length of the preallocated buffer during logging. Its default value is 256. (buffer_length = #samples * (#logged_coordinates + 1))

script_error_logger
~~~~~~~~~~~~~~~~~~~

The script ``script_error_logger`` inherits from ``script_measurement_logger`` and is used to log the error inside
a controller, meaning the measured value minus the desired value.

.. code-block:: xml

    <clone prototype="script_error_logger">
        <member id="controllers" reference_id="tasks.tracking.controllers"/>
        <member id="file_name">{rospkg package_name}/path/{time %F}_file_name.csv</member>
    </clone>

.. Comment to get indent after code-block
..

The parameter ``controllers`` functions as provider. Only controllers are accepted.

The parameter ``provider`` is ignored.

script_measurement_publisher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Script ``script_measurement_publisher`` does not log data inside a file but publishes it.

.. code-block:: xml

    <clone prototype="script_measurement_publisher">
        <member id="provider" reference_id="collections.target_to_tool.chains[0]"/>
        <member id="topic">tool_position</member>
        <member id="coordinates">x,y,z</member>
    </clone>

.. Comment to get indent after code-block
..

The parameter ``provider`` references in contrast to the same parameter in ``script_measurement_logger`` only
one data source that provides the measurement.

The parameter ``topic`` holds the topic name on which to publish. The default value is '**measurements**'.

Skills
-------

Logging skills use ``script_measurement_logger`` and have access to its parameters. Use them by running them in
parallel with other skills by adding the skills to the composition skill ``skill_concurrency``.

skill_log_cartesian
~~~~~~~~~~~~~~~~~~~

The skill ``skill_log_cartesian`` logs the position and orientation of a frame in relationship to a reference
frame.

.. code-block:: xml

    <clone prototype="skill_log_cartesian">
        <member id="measured_frame">tool</member>
        <member id="reference_frame">base_link</member>
        <member id="file_name">{rospkg package_name}/path/{time %F}_file_name.csv</member>
        <member id="filter">a,b,c</member>
    </clone>

.. Comment to get indent after code-block
..

    The parameter ``measured_frame`` holds the id of the frame which data is logged.

    The parameter ``reference_frame`` holds the id of the reference frame for the logged cartesian data.

    The parameters ``provider`` and ``use_simple_filter_keys`` of ``script_measurement_logger`` are already set and
    can not be accessed.

skill_log_force
~~~~~~~~~~~~~~~

The skill ``skill_log_force`` logs the force and torque in a desired frame.

.. code-block:: xml

    <clone prototype="skill_log_force">
        <member id="force_frame">tool</member>
        <member id="file_name">{rospkg package_name}/path/{time %F}_file_name.csv</member>
        <member id="filter">x,y,z</member>
    </clone>

.. Comment to get indent after code-block
..

    The parameter ``force_frame`` holds the id of the frame defining the desired position and axes for measuring
    force and torque.

    The parameters ``provider`` and ``use_simple_filter_keys`` of ``script_measurement_logger`` are already set and
    can not be accessed.



