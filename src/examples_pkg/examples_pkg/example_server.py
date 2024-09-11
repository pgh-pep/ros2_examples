#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class ExampleServerNode(Node):

    def __init__(self):
        super().__init__('example_server')

        # Instantiate a server object w/ service type being AddTwoInts from example_interfaces/srv
        self.srv = self.create_service(srv_type=AddTwoInts, srv_name='add_two_ints', callback=self.add_two_ints_callback)

    # The callback function that is called when a service request received by the server:
    def add_two_ints_callback(self, request, response):
        # a, b, and sum are unique to the AddTwoInts type.
        # ros2 interface show example_interfaces/srv/AddTwoInts
        # ^^^Will give info about example_interfaces/srv/AddTwoInts, will work with any services
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main():
    rclpy.init()
    node = ExampleServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()