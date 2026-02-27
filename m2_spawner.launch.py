from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

import random
import numpy as np

def randomize_poses():

  return randomized

def generate_launch_description():

  pack = ''
  world = 'eletroquad26_m2'
  general_filepath = '/root/PX4-Autopilot/Tools/simulation/gz/worlds/models'

  randomized = randomize_poses()

  for index, x_coord, y_coord, yaw in randomized:
    load_nodes.append(Node(
      package=pack,
      executable='create',
      output='screen',
      parameters=[{
        'world': world,
        'file': general_filepath + '/hang_the_right_wire/transmission_line/pole/model.sdf',
        'string': '', # unused
        'topic': '', # unused
        'name': f'pole{index}',
        'allow_renaming': 'False',
        'x': x_coord,
        'y': y_coord,
        'z': 0.021,
        'R': 0.0, # unused
        'P': 0.0, # unused
        'Y': yaw,
      }],
    ))
    if (index%2)!=0:
      load_nodes.append(Node(
        package=pack,
        executable='create',
        output='screen',
        parameters=[{
          'world': world,
          'file': general_filepath + '/hang_the_right_wire/transmission_line/hose/model.sdf',
          'string': '', # unused
          'topic': '', # unused
          'name': f'wire{index}',
          'allow_renaming': 'False',
          'x': x_coord,
          'y': y_coord,
          'z': 1.721,
          'R': 0.0, # unused
          'P': 0.0, # unused
          'Y': yaw,
        }],
      ))

  load_nodes.append(Node(
    package=pack,
    executable='create',
    output='screen',
    parameters=[{
      'world': world,
      'file': general_filepath + '/hang_the_right_wire/styro_ball/model.sdf',
      'string': '', # unused
      'topic': '', # unused
      'name': 'B A L L',
      'allow_renaming': 'False',
      'x': x_coord,
      'y': y_coord,
      'z': 1.721,
      'R': 0.0, # unused
      'P': 0.0, # unused
      'Y': 0.0, # unused
    }],
  ))


  # Create the launch description and populate
  ld = LaunchDescription()

  # Add the actions to launch all of the create nodes
  for each in load_nodes:
    ld.add_action(load_nodes)

  return ld
