from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "ip",
                default_value="localhost",
                description="IP address for ROS communication",
            ),
            DeclareLaunchArgument(
                "port",
                default_value="10000",
                description="Port number for ROS TCP communication",
            ),
            DeclareLaunchArgument(
                "node_name",
                default_value="server_endpoint",
                description="Name of the node",
            ),
            Node(
                package="ros_tcp_endpoint",
                executable="default_server_endpoint",
                name=LaunchConfiguration("node_name"),
                emulate_tty=True,
                parameters=[
                    {"ROS_IP": LaunchConfiguration("ip")},
                    {"ROS_TCP_PORT": LaunchConfiguration("port")},
                ],
            ),
        ]
    )

