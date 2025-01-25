from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node

package_dir = get_package_share_directory("fast_lio")

CONFIG_COMMON_DIR = PathJoinSubstitution([package_dir, "config"])

rviz_cfg = PathJoinSubstitution([package_dir, "rviz_cfg", "fastlio.rviz"])


def generate_launch_description():
    params = [PathJoinSubstitution([CONFIG_COMMON_DIR, "ouster128.yaml"])]

    fast_lio_node = Node(
        package="fast_lio",
        executable="fastlio_mapping",
        name="fastlio_mapping",
        parameters=[
            params,
            {"use_sim_time": True},
        ],
        output="screen",
    )
    rviz_node = Node(package="rviz2", executable="rviz2", arguments=["-d", rviz_cfg])

    return LaunchDescription([fast_lio_node, rviz_node])
