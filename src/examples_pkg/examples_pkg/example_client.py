#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class ExampleClientNode(Node):
    def __init__(self):
        super().__init__('example_client')

        self.send_request(5, 2)
        
        # Once a service exists, 
    def send_request(self, a, b):
        # Instantiate a client object w/ service type being AddTwoInts from example_interfaces/srv
        # Service type and name must match for the client and server to be able to communicate. 
        self.client = self.create_client(srv_type=AddTwoInts,srv_name='add_two_ints')

        # Loop checks if a service matching the type and name of the client is available every second
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting...')

        # Create a request, set the request parameters a and b
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        # Send the request asynchronously
        # Future can be thought of as a placeholder for the result of call_async()
        future = self.client.call_async(request)

        # Once the request is completed, run a callback function to process the request
        future.add_done_callback(partial(self.callback_for_request, a=a, b=b))


    def callback_for_request(self, future, a, b):
        # Use a try/except in case the service call fails
        try:
            # Extract the results, print the result info
            response = future.result()
            self.get_logger().info(str(a) + " + " +
                                   str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = ExampleClientNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
