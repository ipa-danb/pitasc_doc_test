======
Skills
======

.. toctree::
    :hidden:
    :maxdepth: 1

composition
-----------

* :doc:`skill_concurrency`
  : Hierarchy of skills which are executed simultaneously.
* :doc:`skill_parallel`
  : Hierarchy of skills which are executed simultaneously. Ends with 'succeeded' only if **all** subskills triggered 'succeeded'.
* :doc:`skill_sequence`
  : List of skills which are executed in sequence.
* :doc:`skill_statechart`
  : Group of skills which are connected in a state machine.

.. toctree::
    :hidden:
    :maxdepth: 2

    skill_concurrency
    skill_parallel
    skill_sequence
    skill_statechart

position_controlled
-------------------

* :doc:`loop_target`
  : Models a loop via tool frame and target frame
* :doc:`skill_approach`
  : A skill approaching a target frame in two steps
* :doc:`skill_cartesian`
  : Models a loop via tool frame and target frame
* :doc:`skill_cartesian_bound`
  : Bound for a cartesian value
* :doc:`skill_cartesian_tracking`
  : Keeps on aligning the tool frame with a target frame
* :doc:`skill_cartesian_tracking_pid`
  : Keeps on aligning the tool frame with a target frame
* :doc:`skill_cylindrical`
  : Cylindrical coordinates
* :doc:`skill_cylindrical_positioning`
  : Cylindrical coordinates
* :doc:`skill_cylindrical_tracking`
  : Cylindrical coordinates
* :doc:`skill_hold_duration`
  : Hold the position/orientation on selected axes for duration time.
* :doc:`skill_hold_pose`
  : Hold the position/orientation on selected axes.
* :doc:`skill_joint_space`
  : Models a loop for joint space control
* :doc:`skill_joint_space_bound`
  : Keeps on tracking a joint configuration
* :doc:`skill_joint_space_tracking`
  : Keeps on tracking a joint configuration
* :doc:`skill_lin`
  : Aligns the tool frame with a target frame
* :doc:`skill_lin_time_optimal`
  : LIN movement from the current pose to the target. Follows a time-optimal trajectory with constant acceleration.
* :doc:`skill_lin_trajectory`
  : Moves along given blending points with blending distances to the target frame.
* :doc:`skill_lin_trajectory_base`
  : Base class for linear trajectories.
* :doc:`skill_lin_trajectory_pd`
  : Moves along given blending points with blending distances to the target frame. Controlled by pd controller
* :doc:`skill_log_cartesian`
  : Logs position and/or orientation of a frame w.r.t. a reference skill into a file
* :doc:`skill_partial_lin`
  : A skill that moves to a target frame only in specified axes and holds the other axes in place
* :doc:`skill_ptp`
  : Moves the robot to a target joint configuration
* :doc:`skill_ptp_time_optimal`
  : Keeps on tracking a joint configuration using a time-optimal trajectory
* :doc:`skill_ptp_trajectory`
  : Keeps on tracking a joint configuration
* :doc:`skill_relative_lin`
  : Aligns the tool with an offset relative to the current pose
* :doc:`skill_relative_ptp`
  : A skill that moves to a relative joint configuration
* :doc:`skill_spherical`
  : Spherical coordinates
* :doc:`skill_spherical_positioning`
  : Spherical coordinates
* :doc:`skill_spherical_tracking`
  : Spherical coordinates
* :doc:`skill_wait_for_transform`
  : A skill that keeps the robot position until a transform becomes available

.. toctree::
    :hidden:
    :maxdepth: 2

    loop_target
    skill_approach
    skill_cartesian
    skill_cartesian_bound
    skill_cartesian_tracking
    skill_cartesian_tracking_pid
    skill_cylindrical
    skill_cylindrical_positioning
    skill_cylindrical_tracking
    skill_hold_duration
    skill_hold_pose
    skill_joint_space
    skill_joint_space_bound
    skill_joint_space_tracking
    skill_lin
    skill_lin_time_optimal
    skill_lin_trajectory
    skill_lin_trajectory_base
    skill_lin_trajectory_pd
    skill_log_cartesian
    skill_partial_lin
    skill_ptp
    skill_ptp_time_optimal
    skill_ptp_trajectory
    skill_relative_lin
    skill_relative_ptp
    skill_spherical
    skill_spherical_positioning
    skill_spherical_tracking
    skill_wait_for_transform

force_controlled
----------------

* :doc:`skill_apply_force`
  : Applies a force in the direction of a frame
* :doc:`skill_apply_force_pid`
  : Applies a force in the direction of a frame
* :doc:`skill_force`
  : Models a loop for force control
* :doc:`skill_guarded_approach`
  : A skill that moves along a fixed frame axis until it measures a certain force
* :doc:`skill_guarded_lin`
  : Causes a linear motion until a specified force value is reached
* :doc:`skill_guarded_slide`
  : A skill that moves along a fixed frame axis until it measures a certain force
* :doc:`skill_insert`
  : A skill that pushes and aligns the position
* :doc:`skill_log_force`
  : Logs a force/torque in a desired frame into a file
* :doc:`skill_pivot`
  : Rotates while pushing
* :doc:`skill_push`
  : A skill that pushes and keeps the position
* :doc:`skill_push_duration`
  : A skill that pushes and keeps the position for a certain time.
* :doc:`skill_push_settle`
  : A skill that pushes until the force error is within a region for an acceptable number of samples.
* :doc:`skill_slide`
  : A skill that results in a slide motion in direction of a specified axis
* :doc:`skill_slide_relative`
  : Slides to a target relative to the current position

.. toctree::
    :hidden:
    :maxdepth: 2

    skill_apply_force
    skill_apply_force_pid
    skill_force
    skill_guarded_approach
    skill_guarded_lin
    skill_guarded_slide
    skill_insert
    skill_log_force
    skill_pivot
    skill_push
    skill_push_duration
    skill_push_settle
    skill_slide
    skill_slide_relative

velocity_controlled
-------------------

* :doc:`skill_cartesian_velocity`
  : Track a desired velocity of tool_frame w.r.t. target_frame.
* :doc:`skill_conical_helix`
  : A skill that performs a conical helix around z axis of the specified pivot_frame
* :doc:`skill_cylindrical_helix`
  : A skill that performs a cylindrical helix around z axis of the specified pivot_frame
* :doc:`skill_cylindrical_velocity`
  : Cylindrical coordinates
* :doc:`skill_partial_velocity`
  : A skill that moves along fixed frame axes and holds the other axes in place
* :doc:`skill_partial_velocity_duration`
  : A skill that moves along fixed frame axes and holds the other axes in place
* :doc:`skill_partial_velocity_relative_distance`
  : A skill that moves along fixed frame axes and holds the other axes in place
* :doc:`skill_spherical_velocity`
  : Spherical coordinates

.. toctree::
    :hidden:
    :maxdepth: 2

    skill_cartesian_velocity
    skill_conical_helix
    skill_cylindrical_helix
    skill_cylindrical_velocity
    skill_partial_velocity
    skill_partial_velocity_duration
    skill_partial_velocity_relative_distance
    skill_spherical_velocity

logic
-----

* :doc:`frame_editor_align`
  : Aligns a frame with another frame via ROS service.
* :doc:`frame_editor_copy`
  : Copies a frame via ROS service.
* :doc:`frame_editor_load_yaml`
  : Loads YAML with frame editor.
* :doc:`frame_editor_remove`
  : Remove a frame from the frame_editor via ROS service.
* :doc:`frame_editor_save_yaml`
  : Saves YAML with frame editor.
* :doc:`frame_editor_set`
  : Created a new frame with a give pose via ROS service.
* :doc:`frame_editor_set_parent`
  : Set a new parent frame of a given frame via ROS service.
* :doc:`skill_counter_condition`
  : Branches after a certain number of iterations
* :doc:`skill_idle`
  : A skill that does nothing
* :doc:`skill_idle_duration`
  : A skill that keeps the robot position for a given duration
* :doc:`skill_idle_once`
  : Idles for one cycle, e.g. to execute a script
* :doc:`skill_preempt`
  : Triggers a preempt event

.. toctree::
    :hidden:
    :maxdepth: 2

    frame_editor_align
    frame_editor_copy
    frame_editor_load_yaml
    frame_editor_remove
    frame_editor_save_yaml
    frame_editor_set
    frame_editor_set_parent
    skill_counter_condition
    skill_idle
    skill_idle_duration
    skill_idle_once
    skill_preempt

user
----

* :doc:`skill_user_confirm`
  : Opens a dialog window to receive confirmation from the user.

.. toctree::
    :hidden:
    :maxdepth: 2

    skill_user_confirm
