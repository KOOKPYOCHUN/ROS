#### Topic은 발행(Publish)과 구독(Subscribe)으로 되어있는 개념

#### Topic 조회
 <code>ros2 topic list</code>
#### Topic Data Type(메시지 타입) 조회
#### ros2 topic type or ros2 topic list -t(Topic 전체 메시지 타입 조회)
   <code>ros2 topic type /turtle1/pose</code>

#### 현재 토픽이 발행되고 있는 건지 또는 구독을 대기하고 있는 토픽인지 확인
<code>ros2 topic info</code>
<code> ros2 topic info /turtle1/pose</code>
- 현재 사용할 수 있는 /turtle/pose라는 토픽이 발행되는지 구독대기인 토픽인지 확인
  #### topic info 명령을 사용, 어떤 메시지 타입을 사용하고 구독과 발행하는 노드의 개수를 확인
  #### 일일이 확인이 어려우면 
    <code>ros2 optinc list -v </code> 
    -각 토픽의 이름, 데이터형, 구독 발행 상황 한 번에 확인

#### 토픽 사용을위해 메시지 타입 확인
 - ros2 interface show
  ex) ros2 interface show turtlesim/msg/Pose

#### 토픽을 구독할 수 있는 명령을 이용하여 토픽 구독
 - ros2 topic echo
  ex) ros2 topic echo /turtle1/pose갠

#### 토픽 발행
 - ros2 topic pub --once (or rate <hz>) <topic_name><msg_type>"<arge>"
  #### --once : ros2 topic 명령 후에 한 번만 발행할 것인지
  #### --rate <hz> : 혹은 일정 주기를 가지고 연속 발행할 것인지 ex)--rate 1, 초당 진동수
  #### <topic_name> : 토픽 이름 설정
  #### <msg_type> : 메시지 타입 나열
  #### "<args>" : 입력값 결정

#### geometry_msgs/msg/Twist 데이터 타입의 /turtle1/cmd_vel 토픽을 
   x축 직선 방향으로 2의 속도로 진행하도록 하고 싶다면
 ex) ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x:0.0, y: 0.0, z: 0.0}}"

#### Topic과 Node의 관계를 그림으로 표현
 - rqt_graph
 # 동그라미 : Node
 # 사각형 : Topic


