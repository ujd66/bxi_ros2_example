import os
from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    xml_file_name = "model/xml/elf25/elf25.xml"
    xml_file = os.path.join(get_package_share_path("description"), xml_file_name)

    policy_file_name = "policy/policy.jit"
    policy_file = os.path.join(get_package_share_path("bxi_example_py"), policy_file_name)

    vino_file_name = "policy/model.xml"
    vino_file = os.path.join(get_package_share_path("bxi_example_py"), vino_file_name)

    onnx_file_name = "policy/model.onnx"
    onnx_file = os.path.join(get_package_share_path("bxi_example_py"), onnx_file_name)

    return LaunchDescription(
        [
            Node(
                package="mujoco",
                executable="simulation",
                name="simulation_mujoco",
                output="screen",
                parameters=[
                    {"simulation/model_file": xml_file},
                ],
                emulate_tty=True,
                arguments=[("__log_level:=debug")],
            ),

            Node(
                package="bxi_example_py",
                executable="bxi_example_py",
                name="bxi_example_py",
                output="screen",
                parameters=[
                    {"/topic_prefix": "simulation/"},
                    {"/policy_file": policy_file},
                    {"/vino_file": vino_file},
                    {"/onnx_file": onnx_file},
                ],
                emulate_tty=True,
                arguments=[("__log_level:=debug")],
            ),
        ]
    )
