import numpy as np
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf_transformations import euler_from_quaternion

class ControlNode(Node):
    def __init__(self):
        super().__init__('control')

        self._ts = 0.01
        self._tolerance = 0.3

        self._xk = np.array([0, 0, 0])
        self._xN = np.array([0.6, 0.6, 1.1519])
        self._uk = np.array([0, 0])

        self._K1 = np.array([[-5.0062, -9.0315, 0.0542], [0.0007, 0.0012, -89.0624]])
        self._K2 = np.array([[-3.3469, -9.7200, 0.0659], [0.0005, 0.0016, -89.0378]])

        self._theta_e_min = -0.0873   # -5 degrees
        self._theta_e_max =  0.0873   #  5 degrees

        self._cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)

        self._odometry_subscription = self.create_subscription(Odometry, 'rosbot_base_controller/odom', self.callback_odometry, 10)

        self._sampler = self.create_timer(self._ts, self.callback_sampler)

        self.get_logger().info('Rosbot-2R control node initialized!')

    def callback_sampler(self):

        ex = self._xk - self._xN
        
        w_1 = (self._theta_e_max - ex[2]) / (self._theta_e_max - self._theta_e_min)
        w_2 = 1 - w_1
        
        self._uk = w_1 * self._K1 @ ex + w_2 * self._K2 @ ex

        self.publish_control_signal(self._uk)

        if abs(ex[0]) < self._tolerance and abs(ex[1]) < self._tolerance and abs(ex[2]) < self._tolerance:
            control_msg = Twist()
            self._cmd_vel_publisher.publish(control_msg)
            self.get_logger().info('Target reached, stopping Rosbot.')
        else:
            self.get_logger().info('Rosbot moving towards target.')

    def publish_control_signal(self, uk):
        v, w = uk[0], uk[1]
        v = np.clip(v, -0.8, 0.8)
        w = np.clip(w, -np.pi/2, np.pi/2)
        
        control_msg = Twist()
        control_msg.linear.x = v
        control_msg.angular.z = w
        self._cmd_vel_publisher.publish(control_msg)

    def callback_odometry(self, msg: Odometry):
        _, _, yaw = euler_from_quaternion([msg.pose.pose.orientation.x,
                                           msg.pose.pose.orientation.y,
                                           msg.pose.pose.orientation.z,
                                           msg.pose.pose.orientation.w])
        self._xk = np.array([msg.pose.pose.position.x, msg.pose.pose.position.y, yaw])

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
