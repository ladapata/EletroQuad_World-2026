from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution
from launch_ros.actions import Node

import random
import numpy as np

# angulos válidos

# (0,20)   = [90,57]   ->(-90°)-> [0,327]   = |33°|
# (20,40)  = [27,356]  ->(-90°)-> [297,266] = |31°|
# (40,60)  = [321,300] ->(-90°)-> [231,210] = |21°|
# (60,80)  = [266-235] ->(-90°)-> [176,145] = |31°|
# (80,100) = [204-181] ->(-90°)-> [114,91]  = |23°|

# (0,20)   = [90,57]   ->(+90°)-> [180,147] = |33°|
# (20,40)  = [27,356]  ->(+90°)-> [117,86]  = |31°|
# (40,60)  = [321,300] ->(+90°)-> [51,30]   = |21°|
# (60,80)  = [266-235] ->(+90°)-> [356,325] = |31°|
# (80,100) = [204-181] ->(+90°)-> [294,271] = |23°|

def randomize_poses():

  iter_length = 3 # número de plataformas a serem criadas
  padding = 1 # número que define a distância euclidiana mínima entre as plataformas

  valid_angles = [90, 57, 27, 356, 321, 300, 266, 235, 204, 181]
  interval_chosen = []

  # listas a serem zipadas no final
  indexes = []
  x_coords = []
  y_coords = []
  angles = []

  # inclui a plataforma de decolagem apenas pra simplificar a lógica abaixo
  x_coords.append(0)
  y_coords.append(0)

  for i in range(iter_length): # loop para criar os manômetros
    indexes.append(i+1)
    while True: # loop que garante que todas os manômetros estão a uma distância euclidiana mínima entre si
      chosen_x = round(random.uniform(0, 7) - (7/2), 8)
      chosen_y = round(random.uniform(0, 13) - (13/2), 8)
      distance_flag = False
      for x, y in x_coords, y_coords:
        if pow(chosen_x - x, 2) + pow(chosen_y - y, 2) <= padding:
          distance_flag = True
          break
      if !(distance_flag):
        x_coords.append(chosen_x)
        y_coords.append(chosen_y)
        break

    # escolhe um intervalo entre os ângulos válidos e anexa o valor escolhido dentro do intervalo à lista
    interval = random.randint(1,5)-1
    interval_chosen.append(np.radians(valid_angles[interval]))
    interval_chosen.append(np.radians(valid_angles[interval+1]))
    # TODO: verificar se o sinal deve ser + ou -
    angles.append(random.uniform(interval_chosen[0], interval_chosen[1]) + (np.pi/2))
  
  # "remove a plataforma de decolagem". Apenas garante que todas as listas tenham o mesmo comprimento
  x_coords.pop(0)
  y_coords.pop(0)

  # une todos os parâmetros em uma lista de tuplas
  randomized.append(zip(indexes, x_coords, y_coords, angles))

  return randomized

def generate_launch_description():

  pack = ''
  world = 'eletroquad26_m3'
  general_filepath = '/root/PX4-Autopilot/Tools/simulation/gz/worlds/models'

  pointer_z_offset = 0.85011

  randomized = randomize_poses()

  for index, x_coord, y_coord, pointer_angle in randomized:
    load_nodes.append(Node(
      package=pack,
      executable='create',
      output='screen',
      parameters=[{
        'world': world,
        'file': general_filepath + '/faulty_or_not/manometer/model.sdf',
        'string': '', # unused
        'topic': '', # unused
        'name': f'manometer{index}',
        'allow_renaming': 'False',
        'x': x_coord,
        'y': y_coord,
        'z': 0.871,
        'R': 0.0, # unused
        'P': 0.0, # unused
        'Y': 4.71238898, # 270 degrees
      }],
    ))

# template da pose do ponteiro
# <pose degrees='true'>
# x_coord(+north -south)+0.009 y_coord(+west -east) pointer_offset 0 0 pointer_angle
# </pose>

    load_nodes.append(Node(
      package=pack,
      executable='create',
      output='screen',
      parameters=[{
        'world': world,
        'file': general_filepath + '/faulty_or_not/manometer_pointer/model.sdf',
        'string': '', # unused
        'topic': '', # unused
        'name': f'pointer{index}',
        'allow_renaming': 'False',
        'x': x_coord,
        'y': y_coord,
        'z': 0.87111,
        'R': 0.0, # unused
        'P': 0.0, # unused
        'Y': pointer_angle,
      }],
    ))


  # Create the launch description and populate
  ld = LaunchDescription()

  # Add the actions to launch all of the create nodes
  for each in load_nodes:
    ld.add_action(each)

  return ld
