from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_gazebo_launch 


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("jaka_zu3", package_name="jaka_zu3_moveit_config").to_moveit_configs()
    return generate_gazebo_launch(moveit_config)