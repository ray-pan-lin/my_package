from launch import LaunchDescription
from launch_ros.actions import Node

def generate_lauch_description():
    return LaunchDescription([
        Node(
            package='demo_node_py',
            excutable='listener'
        )
    ])
