from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("jaka_a12", package_name="jaka_a12_moveit_config").to_moveit_configs()
    return generate_moveit_rviz_launch(moveit_config)
