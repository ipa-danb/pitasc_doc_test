===========================
How to start an application
===========================

There are different ways to start a pitasc program, which are explained in the following.

File reader
-----------

The first option is to use the ``pitasc_filereader``. It reads the app file (.xml) and runs one of the applications
inside the ``applications`` member in the file.

.. note::
    See also :doc:`../../fundamentals/application`

The syntax:

.. code-block:: console

    $ pitasc_filereader [<options>] <package> <filename> [<appname>]

.. Comment to get indent after code-block
..

    The ``<package>`` argument specifies the package_name where your application file is present.

    The ``<filename>`` argument specifies the relative path/filename of the application file in the package.

    The ``[<appname>]`` argument allows you to specify a list of application names that get executed. If no
    application name is given and multiple applications are present inside the ``applications`` member of the app
    file, pitasc aborts and a list of all applications inside the ``applications`` member is printed out. If only
    one application is inside the ``applications`` member, pitasc runs it even if the ``[<appname>]`` argument is
    left empty.

    The ``[<options>]`` argument contains a list of options. The following options are available:

        | ``-c``, ``--component-info``:
        | Print in which component the logging happened.

        | ``-v``, ``--verbose``:
        | Print code location of logging statements.

        | ``-l``, ``--log-level`` <loglevel>:
        | Specify which log levels should be printed to the terminal. Possible values: [debug, info, warn, error,
            fatal]. Loglevel "debug" implies verbose logging.

        | ``-t``, ``--trigger-periodic``
        | Uses Trigger with constant trigger rate instead of Joint Topic/ROS based Trigger.

        | ``-h``, ``--help``:
        | Print this usage information.


**Example**

.. code-block:: console

    $ pitasc_filereader pitasc_common examples/beginner/multiple_apps.xml another_application


Executor
--------

The second option to start an application, is to run the ``pitasc_executor_rossrv`` with the following command.

.. code-block:: console

    $ pitasc_executor_rossrv [<options>]

.. Comment to get indent after code-block
..

    The ``[<options>]`` argument specifies a list of options. The following options are available:

        | ``-c``, ``--component-info``:
        | Print in which component the logging happened.

        | ``-v``, ``--verbose``:
        | Print code location of logging statements.

        | ``-l``, ``--log-level`` <loglevel>:
        | Specify which log levels should print to the terminal. Possible values: [debug, info, warn, error,
          fatal]. Loglevel "debug" implies verbose logging.

        | ``-t``, ``--trigger-periodic``
        | Uses Trigger with constant trigger rate instead of Joint Topic/ROS based Trigger.

        | ``-h``, ``--help``:
        | Print this usage information.

This command starts a ros node providing the following ros services:

- ``/pitasc/load`` loads your application.xml file into the executor.

    .. code-block:: console

        $ rosservice call /pitasc/load <package> <filename> [<parameters>]


    The ``<package>`` argument specifies the package_name where your application file is present.

    The ``<filename>`` argument specifies the relative path/filename of the application file in the package.

    The ``[<parameters>]`` argument allows you to change parameters of skills/script/etc. inside the
    ``applications`` member of the app file (this is an optional). Parameters have a name and a value. You can specify the parameter
    of a nested sub-skill by chaining the names with a ``.`` connecting them. Use a ``->`` in front of the value
    of value to indicate that the parameter referenced a parameter with the ``id`` of value. See example below at ``/pitasc/run``

    **Console example**

    .. code-block:: console

        $ rosservice call /pitasc/load "package: 'pitasc_common'
            file_name: 'examples/beginner/multiple_apps.xml'"

    **Python example**

    .. code-block:: python

        import rospy

        from pitasc.srv import Load

        if __name__ == "__main__":
            rospy.init_node("load_srv_caller", anonymous=True)

            load_srv = rospy.ServiceProxy("/pitasc/load", Load)
            resp_load = load_srv.call(package="pitasc_common", file_name="examples/beginner/multiple_apps.xml")


- ``/pitasc/list`` prints out a list of all available applications inside the ``applications`` member of the loaded app file.

    .. code-block:: console

        $ rosservice call /pitasc/list

- ``/pitasc/run`` starts an application from inside the ``applications`` member of your app file.

    .. code-block:: console

        $ rosservice call /pitasc/run <app> [<parameters>]


    The ``<app>`` argument allows you to specify the name of the applications to run. If no application name is
    specified and multiple applications are inside the ``applications`` member of the app file pitasc
    aborts and a list of all applications inside the ``applications`` member is printed out. If only one
    application is inside the ``applications`` member, pitasc runs it even if the ``<app>`` argument is left
    empty.

    The ``[<parameters>]`` argument allows you to change parameters of skills/script/etc. inside the
    ``applications`` member of the app file. Parameters have a name and a value. You can specify the parameter
    of a nested sub-skill by chaining the names with a ``.`` connecting them. Use a ``->`` in front of the value
    of value to indicate that the parameter referenced a parameter with the ``id`` of value.

    **Console example**

    .. code-block:: console

        $ rosservice call /pitasc/run "app: 'another_application'
        parameters:
        - name: 'skills.move_to.max_linear_velocity'
        value: '0.1'
        - name: 'skills.move_to.target_frame'
        value: 'target2'
        - name: 'skills.approach.target_frame'
        value: '->move_to.target_frame'"
    
    **Python example**

    .. code-block:: python

        import rospy

        from pitasc.srv import Run
        from pitasc.msg import Parameter

        if __name__ == "__main__":
            rospy.init_node("run_srv_caller", anonymous=True)

            run_srv = rospy.ServiceProxy("/pitasc/run", Run)

            param1 = Parameter(
                name="skills.move_to.max_linear_velocity",
                value="0.1",
            )
            param2 = Parameter(
                name="skills.move_to.target_frame",
                value="target2",
            )
            param3 = Parameter(
                name="skills.approach.target_frame",
                value="->move_to.target_frame",
            )
            # requires pitasc_common/examples/beginner/multiple_apps.xml being loaded beforehand
            resp = run_srv(app="another_application", parameters=[param1, param2, param3])
    

- ``/pitasc/stop`` stops a running application.

    .. code-block:: console

        $ rosservice call /pitasc/stop

- ``/pitasc/pause`` pauses a running application.

    .. code-block:: console

        $ rosservice call /pitasc/pause

- ``/pitasc/resume`` resumes a paused application.

    .. code-block:: console

        $ rosservice call /pitasc/resume


Pi Teacher (GUI)
----------------
Instead of using rosservice calls directly, another option is to use the ``pi_teacher`` along with the executor node, which gives you a
graphical user interface for calling the ros services.

.. code-block:: console

    $ rqt -s pi_teacher


Python API
----------
You can also use the python API to use pitasc directly within python. Please note that this feature is still experimental.

.. code-block:: python

    import os
    import sys

    import rospy

    # pitasc
    from pitasc.model import Model
    from cppitasc.runtime import Executor, roscpp_init
    from cppitasc.package_path import get_package_path

    if __name__ == "__main__":

        # ROS
        rospy.init_node("pitasc", log_level=rospy.INFO)

        # init pitasc
        roscpp_init("pitasc", sys.argv)

        # Load file
        model = Model()
        file_name = os.path.join(get_package_path("pitasc_common"), "examples/beginner/multiple_apps.xml")
        model.import_file(file_name)

        # Execute
        executor = Executor(model)

        executor.run("another_application", {})
