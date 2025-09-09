#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from concurrent.futures import Future
from rclpy.action.client import ClientGoalHandle


# ros2 interface show pep_example_interfaces/action/Fibonacci
from pep_example_interfaces.action import Fibonacci


class ExampleActionClient(Node):
    def __init__(self):
        super().__init__("fibonacci_action_client")
        self._action_client = ActionClient(self, Fibonacci, "fibonacci")

        self.send_goal(10)

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        # Send the request
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        # Handle the request with a callback function
        self._send_goal_future.add_done_callback(self.goal_callback)

    def feedback_callback(self, feedback_msg: Fibonacci.Feedback):
        # Called whenever server gives feedback
        feedback = feedback_msg.feedback
        self.get_logger().info(f"got feedback: {feedback.partial_sequence}")

    def goal_callback(self, future: Future):
        # first callback ensures request is acceepted
        goal_handle: ClientGoalHandle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("goal rejected")
            return

        self.get_logger().info("processing accepted goal...")

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.result_callback)

    def result_callback(self, future: Future):
        # Second callback handles actual result data
        # you can do just one callback, but this allows for more granular control
        result: Fibonacci.Result = future.result().result
        self.get_logger().info(f"Result: {result.sequence}")


def main(args=None):
    rclpy.init(args=args)

    action_client = ExampleActionClient()
    try:
        rclpy.spin(action_client)
    finally:
        action_client.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
