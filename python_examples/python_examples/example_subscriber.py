#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class ExampleSubscriberNode(Node):
    def __init__(self):
        super().__init__("example_subscriber")

        # Creates a subscriber instance on the topic "pep_topic"

        # "pep_topic" will be a String type from example_interfaces.msg
        # Will run callback function whenever receives msg's

        # qos_profile is the 'backflow', or the number of previous published msg's stored in memory
        self.subscription = self.create_subscription(String, "pep_topic", self.callback_subscriber, 10)

        self.get_logger().info(message="Started example subscriber...")

    def callback_subscriber(self, msg: String):
        self.get_logger().info(f"we need to find {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = ExampleSubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
