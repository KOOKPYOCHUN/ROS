#### ROS2 Galactic Desktop 버전의 경우 Turtlesim 설치되어 있음
#### 설치 안 되어있을 경우

#### 설치
```
sudo apt install ros-galactic-turtlesim
```
#### 실행
```
ros2 run turtlesim turtlesim_node
```
### Note
- ROS2 노드 실행 시 
```
ros2 run <PKG Name> <Node Name>
ex) ros2 run turtlesim turtlesim_node
```
- 터미널 실행시 opt 경로의 set.bash를 읽는 source 명령을 터미널을 실행될 때마다 읽어들이는 홈 경로의 .bashrc 파일에 명렬어를 넣음
- alias 설정을 이용하여 galactic 이라는 명령어 만듦

- 노드의 정보를 알고 싶을때
```
ros2 node info /<Node Name>
ex) ros2 node info
```
