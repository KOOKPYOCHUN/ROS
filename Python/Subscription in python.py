import rclpy as rp ## ROS2를 Python에서 사용 가능, rclpy를 rp로 사용
form turtlesim.msg import Pose ## turtlesim/msg/Pose 데이터 타입을 Python에서 사용하기 위해 import

rp.init() # Python에서 rclpy 초가화
test_node = rp.create_node('sub_test') # sub_test 노드 생성

## Note ##
ros2 node list 사용하여 노드 생성되었는지 확인 가능
