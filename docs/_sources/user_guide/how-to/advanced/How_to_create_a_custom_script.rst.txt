=============================
How to create a custom script
=============================

This guide explains how to create a custom script. Scripts consist of two parts, the structure which is defined inside a ``.xml`` and the implementation which is inside a ``.cpp`` file.

First, create the ``.xml``, ``.cpp`` and ``.hpp`` files in a ros package.  Good practice is to save the custom script in a ``models`` folder with the naming convention ``script_[script_name].xml``. Save your script.cpp file in the ``/srs/scripts`` directory and the scripts.hpp in the ``include/package_name/scripts`` directory of your package and use the following naming convention ``script_[script_name].cpp`` / ``script_[script_name].hpp``.


.. code-block:: text
    :emphasize-lines: 7,10,14

    package_name
    ├── examples
    ├── include
    |   └── package_name
    |       ├── monitors
    |       ├── scripts
    |       |   └── script_[script_name].hpp <-- Your script.hpp file
    |       └── ...
    ├── models
    |   └── script_[script_name].xml    <-- Your script.xml file
    ├── src
    |   ├── monitors
    |   ├── scripts
    |   |   └── script_[script_name].cpp     <-- Your script.cpp file
    |   └── ...
    ├── package.xml
    └── CMakeLists.txt
    

XML
---

To create a script, include the base type ``script`` (see below). Add the include statement at the start of the ``<models>`` tag with the following syntax.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 3

    <pitasc>
        <models>
            <include package="package_name" file="models/script_[script_name].xml.xml"/>
            ...

.. note::
    | To include the base script, use this include statement
    | ``<include package="pitasc_library" file="models/pitasc.xml" />``


The script gets added right after the include statements in the ``<models>`` by using the ``<type>`` tags.

.. code-block:: xml
    :emphasize-lines: 1

    <type id="script_[script_name]" prototype="{base script}">
        <!-- script body -->
    </type>

.. Comment to get indent after code-block
..

    The ``id``, i.e., the script name, should be unique and descriptive.

    The attribute ``prototype`` refers to the base script, which is the basis of the new script. If you do not extend an existing script, use ``script``.


Set the metadata inside the ``<meta>`` tag of the script.

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

    The parameter ``description`` contains a description. Describe the script in as much detail as needed to understand the script completely. This description can be used to create the automatically generated documentation.

    The parameter ``categories`` should include the categories of the base script.. An exception to this is the internal category of base-scripts. The category has no special meaning, but can help to sort the scripts, e.g., in a documentation or a GUI. Examples for categories are the entries of :doc:`../../../xml_reference/scripts/index`.

    The parameter ``visibility`` determines how a script is shown inside the documentation. It can be set to required, basic, expert and hidden. In most cases, basic visibility should be used.

    The parameter ``implementation`` is a dictionary in which the implementations are placed.

Pitasc implementations are ocoros, since the project used orocos state machine in the past.

.. code-block:: xml

    <member id="implementation">
        <clone prototype="orocos">
            <member id="package">[package_name]_scripts</member>
            <member id="component">CppScriptClassName</member>  <!-- Name of the c++ script class -->
        </clone>
    </member>

.. Comment to get indent after code-block
..

    The parameter ``package`` defines the c++ library containing the component, use ``[package_name]_scripts``. Must be used in the `CMakeLists.txt` file to create the c++ library (see below).

    The parameter ``component`` links to the C++ implemented class using the class name as the value.

Inside the ``<data>`` tag is where the parameters of the script are placed.

.. rstcheck: ignore-next-code-block
.. code-block:: xml
    :emphasize-lines: 4

    ...
    </meta>
    <data>
        <!-- script parameter definition -->
    </data>

.. Comment to get indent after code-block

    How to add parameters is explained in: :doc:`How_to_add_a_parameter_to_a_skill_monitor_etc`


| **Example**
| This is the xml definition of the ``script_temp_frame``, existing in the pitasc library.

.. code-block:: xml

    <type id="script_temp_frame" prototype="script_kinematic_graph">
        <meta>
            <member id="description">Creates a temporary frame that lives as long as the parent skill is active.</member>
            <member id="categories">frames</member>
            <member id="implementation">
                <clone prototype="orocos">
                    <member id="package">cppitasc_kinematics</member>
                    <member id="component">ScriptTempFrame</member>
                </clone>
            </member>
        </meta>
        <data>
            <type id="frame" prototype="string_parameter">
                <meta>
                    <member id="description">Name of the frame to be created</member>
                    <member id="visibility">required</member>
                </meta>
            </type>

            <type id="source" prototype="string_parameter">
                <meta>
                    <member id="description">Name of the frame to be copied</member>
                    <member id="visibility">required</member>
                </meta>
            </type>

            <type id="parent" prototype="string_parameter">
                <meta>
                    <member id="description">Name of the parent frame to of 'frame'</member>
                    <member id="visibility">required</member>
                </meta>
            </type>
        </data>
    </type>

C++
---

Create the Script class by inheriting from another script. In most cases, you will inherit from the base script class ``Script`` in the package **cppitasc**

.. rstcheck: ignore-next-code-block
.. code:: c++

    class ScriptName : public Script {
        //Add stuff here
    };

.. note::

    | The base script class can be included with the following include statement
    | ``#include "cppitasc/coordination/script.hpp"``


The implementation of the script uses multiple functions that are called at different parts of the skill execution. The following functions are available for use. The most often used ones are highlighted.

.. code-block:: text
    :emphasize-lines: 1,3,4,7

    init()        : Called in the factory after object creation (more or less the constructor). Read the xml parameters here.
    onConfigure() : Called when an application is started to configure the component.
    onStart()     : Called when a component is started (when a skill is entered).
    onUpdate()    : Called on Update (each pitasc cycle)
    onPause()     : Called when a component is paused
    onResume()    : Called when a component is resumed
    onStop()      : Called when a component is stopped (when a skill is exited).
    onCleanup()   : Called when an application is stopped to cleanup the component.

To add logic to the scripts, override the needed functions. The header file:

.. rstcheck: ignore-next-code-block
.. code-block:: c++
    :emphasize-lines: 3

    class ScriptName : public Script {
    public:
        bool onStart() override;
        //Add more stuff here
    };

At the end of your implementation of the function, call the base type function and return its result (if no ``void`` type).

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 4

    bool ScriptName::onStart()
    {
        // some implementation
        return Script:onStart()
    }

To access parameters defined in the ``.xml`` see :doc:`How_to_access_parameter_inside_cpp_files`

Add the script by appending the following syntax to the end of the ``script_[script_name].cpp`` file.

.. rstcheck: ignore-next-code-block
.. code-block:: cpp

    RUNTIME_COMPONENT(ScriptName)

| **Example**
| In this example from the pitasc library, the declaration and implementation are both in the cpp file (no header file).

.. rstcheck: ignore-next-code-block
.. code-block:: cpp
    :emphasize-lines: 2, 10, 33, 35, 46, 52, 55

    #include <kdl/frames.hpp>
    #include "cppitasc/coordination/script.hpp"
    #include "cppitasc/kinematic_tree.hpp"
    #include "cppitasc/utils/tf_publisher.hpp"

    class ScriptTempFrame : public Script {
    public:
        explicit ScriptTempFrame(const string& name) : Script(name) {}

        bool init(Dict& params) override
        {
            // Kinematic Tree
            auto peer = extract_type(params["kinematic_graph"], shared_ptr<RuntimeObject>);
            tree_ = dynamic_cast<KinematicTree*>(peer.get());

            frame_id_ = extract_type(params["frame"], string);
            extract(params["source"], source_);
            extract(params["parent"], parent_);
            bool tf_broadcast = extract_type(params["tf_broadcast"], bool);
            tf_publisher_.setBroadcast(tf_broadcast);

            auto result = tree_->addElement(frame_id_, parent_, frame_id_ + "-" + parent_ + "-temp");
            if (result) {
                joint_ = result.value();
            } else {
                throw std::runtime_error("ScriptTempFrame: Frame '" + frame_id_ + "' already exists!");
            }

            setDependencies({});
            return Script::init(params);
        }

        bool onConfigure() final { return Script::onConfigure(); }

        bool onStart() override
        {
            // Update pose
            if (!tree_->lookup(parent_, source_, frame_)) {
                throw std::runtime_error("ScriptTempFrame: Lookup from '" + parent_ + "' to '" + source_
                                        + "' not possible");
            }
            tree_->setTransform(joint_, frame_);
            return Script::onStart();
        }

        void onUpdate(const Tick& tick) override
        {
            tf_publisher_.publishFrame(frame_, parent_, frame_id_);
            return Script::onUpdate(tick);
        }

        void onStop() final { return Script::onStop(); }
    };

    RUNTIME_COMPONENT(ScriptTempFrame)


To build the script with ``catkin build package_name``, add the following lines to the CMakeLists.txt.

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
       LIBRARIES ${PROJECT_NAME}_scripts
    #  CATKIN_DEPENDS other_catkin_pkg
    #  DEPENDS system_lib
    )

    include_directories(
      ${catkin_INCLUDE_DIRS}
    )

    add_library(${PROJECT_NAME}_scripts
      src/scripts/script_[script_name].cpp
    )
    target_link_libraries(${PROJECT_NAME}_scripts
      ${catkin_LIBRARIES}
    )

    install(TARGETS ${PROJECT_NAME}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
    )

After sourcing, you are able to use the script within a pitasc skill, as described in :doc:`../beginner/How_to_attach_a_script_to_a_skill`.
