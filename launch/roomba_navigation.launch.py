import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    nav_config_path = os.path.join(get_package_share_directory('roomba_navigation'),'config','config.yaml')

    return LaunchDescription([
        IncludeLaunchDescription(
            launch_description_source=([
                get_package_share_directory('roomba_navigation'),
                '/launch/roomba_bringup.launch.py'
            ])
        ),
        IncludeLaunchDescription(
            launch_description_source=([
                get_package_share_directory('create_bringup'),
                '/launch/create_2.launch'
            ]),
            launch_arguments={
                'params_file': nav_config_path
            }.items()
        ),
        IncludeLaunchDescription(
            launch_description_source=([
                get_package_share_directory('ldlidar_node'),
                '/launch/ldlidar_with_mgr.launch.py'
            ])
        ),
        Node(
            ## Configure the TF of the robot to the origin of the map coordinatesf
            package='tf2_ros',
            executable='static_transform_publisher',
            namespace='',
            output='screen',
            arguments=['0.10', '0.0', '0.05', '-1.5708', '0.0', '0.0', 'base_footprint', 'ldlidar_base']
        )
        
    ])