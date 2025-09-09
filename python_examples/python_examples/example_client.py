#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
import time

# ros2 interface show pep_example_interfaces/srv/CalcRectArea
from pep_example_interfaces.srv import CalcRectArea


class ExampleClient(Node):
    def __init__(self):
        super().__init__("area_calculator_client")

        # init client w/ CalcRectArea service type
        self.client = self.create_client(CalcRectArea, "calc_rect_area")

        # Wait for the service to be available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service calc_rect_area not available, waiting...")

        self.get_logger().info("service available!")

        # send requests
        self.send_request(x=1.0, y=2.0)
        time.sleep(2)
        self.send_request(x=10.0, y=12.0)
        time.sleep(2)
        self.send_request(x=1.0, y=-1.0)

    def send_request(self, x: float, y: float):
        # ensure service is still up
        if not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Service not available")
            return

        # Create request
        request = CalcRectArea.Request()
        request.x = x
        request.y = y

        self.get_logger().info(f"requesting area of rect x = {x}, y = {y}")

        # Send async request
        future = self.client.call_async(request)

        # Add callback w/ request info for context
        future.add_done_callback(partial(self.response_callback, x=x, y=y))

    def response_callback(self, future, x: float, y: float):
        try:
            response: CalcRectArea.Response = future.result()

            if response.success:
                self.get_logger().info(f"Area of rect w/ x = {x}, y = {y} = {response.area:.2f}, also {response.message}")
            else:
                self.get_logger().warn(f"Failed getting area of rect w/ x = {x}, y = {y}; {response.message}")

        except Exception as e:
            self.get_logger().error(f"Service call failed for rect w/ x = {x}, y = {y}: {str(e)}")


def main(args=None):
    rclpy.init(args=args)

    example_client = ExampleClient()

    try:
        rclpy.spin(example_client)
    finally:
        example_client.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
