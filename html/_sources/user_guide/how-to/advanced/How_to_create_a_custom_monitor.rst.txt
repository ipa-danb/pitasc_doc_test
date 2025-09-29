==============================
How to create a custom monitor
==============================

This guide explains how to create a monitor. Monitors consist of two parts, the structure which is defined inside a ``.xml`` and the implementation which is inside a ``.cpp`` file.

First, create the ``.xml``, ``.cpp`` and ``.hpp`` files in a ros package.  Good practice is to save the custom monitor in a ``models`` folder with the naming convention ``monitor_[monitor_name].xml``. Save your monitor.cpp file in the ``/srs/monitors`` directory and the monitor.hpp in the ``include/package_name/monitors`` directory of your package and use the following naming convention ``monitor_[monitor_name].cpp`` / ``monitor_[monitor_name].hpp``.


.. code-block:: text
    :emphasize-lines: 6,10,13

    package_name
    ├── examples
    ├── include
    |   └── package_name
    |       ├── monitors
    |       |   └── monitor_[monitor_name].hpp <-- Your monitor.hpp file
    |       ├── scripts
    |       └── ...
    ├── models
    |   └── monitor_[monitor_name].xml    <-- Your monitor.xml file
    ├── src
    |   ├── monitors
    |   |   └── monitor_[monitor_name].cpp     <-- Your monitor.cpp file
    |   ├── scripts
    |   └── ...
    ├── package.xml
    └── CMakeLists.txt


XML
---

To create a monitor, first include the parent monitor. Add the include statement at the start of the ``<models>`` tag with the following syntax.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="package_name" file="models/monitor_[monitor_name].xml"/>
            ...

.. note::
    | To include the base monitor, use this include statement.
    | ``<include package="pitasc_library" file="models/pitasc.xml" />``

The monitor has to be added right after the include statements in the ``<models>`` by using the ``<type>`` tags.

.. code-block:: xml
    :emphasize-lines: 1

    <type id="monitor_[monitor_name]" prototype="{base monitor}">
        <!-- monitor body -->
    </type>

.. Comment to get indent after code-block
..

    The ``id``, i.e., the monitor name, should be unique and descriptive.

    The attribute ``prototype`` refers to the base monitor, which is the basis of the new monitor. If you do not extend an existing monitor, use ``monitor``.


Set the metadata inside the ``<meta>`` tag of the monitor.

.. code-block:: xml

    <meta>
        <member id="description">Description</member>
        <member id="categories">category_1, category_2</member>
        <member id="visibility">basic</member>
        <member id="implementation">
            <!-- Implementation details -->
        </member>
    </meta>

.. Comment to get indent after code-block
..

    The parameter ``description`` contains a description. Describe the monitor in as much detail as needed to understand the monitor completely. This description is used to create the automatically generated documentation.

    The parameter ``categories`` should include the categories of the base monitor.. An exception to this is the internal category of base-monitors. The category has no special meaning, but can help to sort the monitors, e.g., in a documentation or a GUI. Examples for categories are the entries of :doc:`../../../xml_reference/monitors/index`.

    The parameter ``visibility`` determines how a monitor is shown inside the documentation. It can be set to required, basic, expert or hidden. In most cases, basic visibility should be used.

    The parameter ``implementation`` is a dictionary in which the implementations are placed.

Pitasc implementations are ocoros, since the project used orocos state machine in the past.

.. code-block:: xml

    <member id="implementation">
        <clone prototype="orocos">
            <member id="package">[package_name]_monitors</member>
            <member id="component">CppMonitorClassName</member>  <!-- Name of the c++ monitor class -->
        </clone>
    </member>

.. Comment to get indent after code-block
..

    The parameter ``package`` defines the c++ library containing the component, use ``[package_name]_monitors``. Must be used in the `CMakeLists.txt` file to create the c++ library (see below).

    The parameter ``component`` links to the C++ implemented class using the class name as the value.

Inside the ``<data>`` tag is where every parameter of the monitor is placed.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 4

    ...
    </meta>
    <data>
        <!-- monitor parameter definition -->
    </data>

.. Comment to get indent after code-block

    How to add parameters is explained in: :doc:`How_to_add_a_parameter_to_a_skill_monitor_etc`


| **Example**
| This is the xml definition of the ``monitor_duration``, existing in the pitasc library.

.. code-block:: xml

    <type id="monitor_duration" prototype="monitor">
        <meta>
            <member id="description">Triggers after a certain time.</member>
            <member id="categories">logic</member>
            <member id="implementation">
                <clone prototype="orocos">
                    <member id="package">cppitasc_monitors</member>
                    <member id="component">DurationMonitor</member>
                </clone>
            </member>
        </meta>
        <data>
            <type id="duration" prototype="float_parameter">
                <meta>
                    <member id="description">The amount of time to wait until triggering</member>
                    <member id="visibility">required</member>
                </meta>
            </type>
        </data>
    </type>

C++
---

Create the monitor class by inheriting from another monitor. In most cases, the monitor will inherit from the base monitor class ``Monitor`` in the package **cppitasc**

.. rstcheck: ignore-next-code-block
.. code:: c++

    class MonitorName : public Monitor {
        //Add stuff here
    };

.. note::

    | The base monitor class can be included with the following include statement
    | ``#include "cppitasc/coordination/monitor.hpp"``


The implementation of the monitor uses multiple functions that are called at different parts of the skill execution. The following functions are available for use. The most often used ones are highlighted.

.. code-block:: text
    :emphasize-lines: 1,3,4,7

    init()        : Called in the factory after object creation (more or less the constructor). Read the xml parameters here.
    onConfigure() : Called when an application is started to configure the component.
    onStart()     : Called when a component is started (when a skill is entered).
    onUpdate()    : Called on Update
    onPause()     : Called when a component is paused
    onResume()    : Called when a component is resumed
    onStop()      : Called when a component is stopped (when a skill is exited).
    onCleanup()   : Called when an application is stopped to cleanup the component.

To add logic to the monitor, override the needed functions. The header file:

.. rstcheck: ignore-next-code-block
.. code-block:: c++
    :emphasize-lines: 3

    class MonitorName : public Monitor {
    public:
        bool onStart() override;
        //Add more stuff here
    };

At the end of your implementation of the function, call the base type function and return its result (if no ``void`` type).

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 4

    bool MonitorName::onStart()
    {
        // some implementation
        return Monitor::onStart()
    }

To access parameters defined in the ``.xml`` see :doc:`How_to_access_parameter_inside_cpp_files`

To trigger the event, for example on successful completion of the skill, use the ``fire()`` function inherited from the monitor base class ``Monitor``.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 6

    bool MonitorName::update()
    {
        //some implementation

        if (condition) {
            fire();
        }

        return Monitor::update();
    }

Using the `Operator` class makes it easy to check if the condition is met, and change the condition by only editing the operator parameter inside the xml. See :doc:`How_to_use_the_operator_class`.

Add the monitor by appending the following syntax to the end of the ``monitor_[monitor_name].cpp`` file.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp

    RUNTIME_COMPONENT(MonitorName)


| **Example**
| In this example from the pitasc library, the declaration and implementation are both in the cpp file (no header file).

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 3, 10, 19, 21, 28, 37

    #include <chrono>
    #include <boost/algorithm/string/predicate.hpp>
    #include "cppitasc/coordination/monitor.hpp"
    #include "cppitasc/coordination/skills.hpp"

    class DurationMonitor : public Monitor {
    public:
        explicit DurationMonitor(const string& name) : Monitor(name){}

        bool init(Dict& params) override
        {
            pi_debug("Init component '{}'", getName());
            extract(params["duration"], duration_);
            setDependencies({});
            return Monitor::init(params);
        }

    protected:
        bool onStart() final { return Monitor::onStart(); }

        void onUpdate(const Tick& t) final
        {
            if (just_started_) {
                time_ = t;
            }
            auto elapsed_seconds = std::chrono::duration_cast<std::chrono::duration<double>>(t - time_).count();
            if (elapsed_seconds >= duration_) {
                fire();
            }
        }

    protected:
        std::chrono::high_resolution_clock::time_point time_;
        double duration_{0.0};
    };

    RUNTIME_COMPONENT(DurationMonitor)


To build the monitor with ``catkin build package_name``, add the following lines to the CMakeLists.txt.

.. code:: cmake

    cmake_minimum_required(VERSION 3.0.2)
    project(package_name)

    add_compile_options(-std=c++17)

    ## Find catkin macros and libraries
    find_package(catkin REQUIRED COMPONENTS
      cppitasc
      # possibly other libraries
    )

    catkin_package(
       INCLUDE_DIRS include
       LIBRARIES ${PROJECT_NAME}_monitors
    #  CATKIN_DEPENDS other_catkin_pkg
    #  DEPENDS system_lib
    )

    include_directories(
      ${catkin_INCLUDE_DIRS}
    )

    add_library(${PROJECT_NAME}_monitors
      src/monitors/monitor_[monitor_name].cpp
    )
    target_link_libraries(${PROJECT_NAME}_monitors
      ${catkin_LIBRARIES}
    )

    install(TARGETS ${PROJECT_NAME}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
    )

After sourcing, you are able to use the monitor within a pitasc skill, as described in :doc:`../beginner/How_to_attach_a_monitor_to_a_skill`.