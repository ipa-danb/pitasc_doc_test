========================
Skill wait_for_transform
========================

This skill waits and holds the robot position until a transform for the specific frame gets published

For most skills, the transform to e.g. its goal needs to be published already, otherwise the execution will fail

The skill `wait_for_transform` makes sure, that this requirement is fulfilled.


`ROS Documentation <http://wiki.ros.org/tf/Tutorials/tf%20and%20Time%20%28C%2B%2B%29>`_