
import numpy as np

# Compatibility fix for older urdfpy
if not hasattr(np, "float"):
    np.float = float

from urdfpy import URDF

# Load robot
robot = URDF.load("robot.urdf")

print("Robot loaded successfully!")
print("Robot name:", robot.name)

print("\nLinks:")
for link in robot.links:
    print("-", link.name)

print("\nJoints:")
for joint in robot.joints:
    print("-", joint.name, "|", joint.joint_type)

print("\nTotal links:", len(robot.links))
print("Total joints:", len(robot.joints))
