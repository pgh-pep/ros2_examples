#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyCustomNode(Node): 
    def __init__(self):
        # Change to node name (usually also filename).
        # Make executable w/ chmod +x fileName.py
        # Make sure to add new nodes to setup.py entry_points
        super().__init__("node_name")


def main(args=None):
    rclpy.init(args=args) # Start ROS comms
    node = MyCustomNode() # Initialize node object
    rclpy.spin(node) # Run node until shutdown
    rclpy.shutdown() # End ROS comms


if __name__ == "__main__":
    main()