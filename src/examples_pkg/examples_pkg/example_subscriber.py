#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher")

        # Creates a subscriber instance on the topic "pep_topic"
        # "pep_topic" will be a String type from example_interfaces.msg
        # Will run callback function whenever recieves msg's
        # qos_profile is the 'backflow', or the number of previous published msg's stored in memory
        self.subscription = self.create_subscription(String, 'pep_topic', self.callback_subscriber, 10)

        # Prints statement to terminal
        self.get_logger().info(message="Intializing Example Subscriber:")

    def callback_subscriber(self,msg):
        self.get_logger().info(f"I think that {msg.data}")
        

    # self.subscription = self.create_subscription(
    #         String,
    #         'topic',
    #         self.listener_callback,
    #         10)
    #     self.subscription  # prevent unused variable warning

    # def listener_callback(self, msg):
    #     self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
