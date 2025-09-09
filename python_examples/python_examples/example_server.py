#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# ros2 interface show pep_example_interfaces/srv/CalcRectArea
from pep_example_interfaces.srv import CalcRectArea


class ExampleServer(Node):
    def __init__(self):
        super().__init__("area_calculator_server")

        # Create the service
        self.service = self.create_service(CalcRectArea, "calc_rect_area", self.calc_area_callback)

        self.get_logger().info("server is waiting...")

    def calc_area_callback(self, request: CalcRectArea.Request, response: CalcRectArea.Response):
        x = request.x
        y = request.y

        self.get_logger().info(f"request recieved: x={x}, y={y}")

        # perform operations on the request
        if x <= 0 or y <= 0:
            response.success = False
            response.area = 0.0
            response.message = f"Invalid dimensions: both x and y must be positive (got x={x}, y={y})"
            self.get_logger().warn(response.message)
        else:
            area = x * y
            response.success = True
            response.area = area
            response.message = f"sucessfully calculated area: {x} * {y} = {area}"
            self.get_logger().info(response.message)

        # return your response
        return response


def main(args=None):
    rclpy.init(args=args)

    example_server = ExampleServer()
    try:
        rclpy.spin(example_server)
    finally:
        example_server.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
