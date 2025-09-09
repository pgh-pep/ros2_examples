#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class ExamplePublisherNode(Node):
    def __init__(self):
        super().__init__("example_publisher")
        # Creates a publisher instance on the topic "pep_topic"
        # Communicates with a String msg from example_interfaces.msg
        # To get additional details about String msgs, use:
        #     `ros2 interface show example_interfaces/msg/String`
        
        # qos_profile is the 'backflow', or the number of previous published msg's stored in memory
        self.publisher_ = self.create_publisher(msg_type=String, topic="pep_topic", qos_profile=10)

        # Creates a timer that runs a callback function every .5 seconds.
        self.timer_ = self.create_timer(timer_period_sec=0.5, callback=self.publish_news)

        self.get_logger().info(message="Started example publisher...")

    def publish_news(self):
        # Creates an example_interfaces/msg/String message instance
        msg = String()
        msg.data = "jobs"

        # Publish the msg:
        self.publisher_.publish(msg=msg)


def main(args=None):
    rclpy.init(args=args)
    node = ExamplePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
