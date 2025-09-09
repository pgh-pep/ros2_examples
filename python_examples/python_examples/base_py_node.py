#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


# Make sure your file is executable w/ `chmod +x fileName.py`

class MyCustomNode(Node):
    def __init__(self):
        # If using `ament_python`, make sure to add new nodes to `setup.py` `entry_points`
        # If using `ament_cmake_python`, you're good
        # Either way add ROS dependencies to your `packages.xml`
        super().__init__("insert_node_name")

        self.get_logger().info("base node started!")


# Unless using ROS2 components, each node should have a top-level execution:
def main(args=None):
    rclpy.init(args=args)  # Start ROS comms
    node = MyCustomNode()  # Initialize node
    rclpy.spin(node)  # Run node until shutdown
    rclpy.shutdown()  # End ROS comms


if __name__ == "__main__":
    main()
