import rclpy as rp ## ROS2를 Python에서 사용 가능, rclpy를 rp로 사용
form turtlesim.msg import Pose ## turtlesim/msg/Pose 데이터 타입을 Python에서 사용하기 위해 import

rp.init() # Python에서 rclpy 초가화
test_node = rp.create_node('sub_test') # sub_test 노드 생성

def callback(data): ## 토픽을 받을 때마다 실행하게 하는 함수, X, Y, Theta를 출력해서 확인하기 위한 callback 함수 구성
  print("--->")
  print("/turtle1/pose : ", data)
  print("X : ", data.x)
  print("Y : "data.y)
  print("Theta : ", data.theta)

test_node.create_subscription(Pose, '/turtle1/pose', callback, 10) # test_node에서 create_subscription을 하기 형식으로 호출
# test_node.create_subscription(<data_type>, '<topic_name>', <callback>, <QoS History>) , <QoS History> = 저장할 샘플의 수

rp.spin_onca(test_node) # spin_once 명령을 통해 test_node를 rp.spin_onca(test_node)라고 지정, 해당 노드 구독 


## Note ##
ros2 node list 사용하여 노드 생성되었는지 확인 가능
spin_noce는 토픽을 한 번만 받는 명령
spin은 토픽을 무한하게 구독
