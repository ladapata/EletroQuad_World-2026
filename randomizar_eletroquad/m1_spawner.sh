# def randomize_poses():
# 
#   iter_length = 7 # número de plataformas a serem criadas
#   padding = 0.6 # número que define a distância euclidiana mínima entre as plataformas
# 
#   # listas de itens para spawnar
#   shapes = ['hexagon', 'star', 'triangle']
#   nums = ['nums/num_3', 'nums/num_4', 'nums/num_5']
# 
#   #TODO: FAZER ELA CRIAR UM ARQUIVO DE IMAGEM E BOTAR NA PASTA CERTA
#   # criação da imagem ArUco
#   chosen_factor = random.randint(3,5)
#   aruco = generate_aruco(chosen_factor)
# 
#   # listas a serem zipadas no final
#   indexes = []
#   x_coords = []
#   y_coords = []
#   chosen_shapes = []
#   chosen_nums = []
# 
#   # inclui a plataforma de decolagem apenas pra simplificar a lógica abaixo
#   x_coords.append(0)
#   y_coords.append(0)
# 
#   # variáveis de controle
#   valid_platform = False
#   aruco_shape = ''
#   aruco_num = ''
# 
#   for i in range(iter_length): # loop pra criar as plataformas
#     indexes.append(i)
#     while True: # loop que garante que todas as plataformas estão a uma distância euclidiana mínima entre si
#       chosen_x = round(random.uniform(0, 7) - (7/2), 8)
#       chosen_y = round(random.uniform(0, 13) - (13/2), 8)
#       distance_flag = False
#       for x, y in x_coords, y_coords:
#         if pow(chosen_x - x, 2) + pow(chosen_y - y, 2) <= padding:
#           distance_flag = True
#           break
#       if !(distance_flag):
#         x_coords.append(chosen_x)
#         y_coords.append(chosen_y)
#         break
#     if valid_platform: # caso já exista uma plataforma válida...
#       while True: # garante que não existe outra plataforma válida para o aruco dado
#         shape = shapes(random.randint(0,2))
#         num = shapes(random.randint(0,2))
#         if (shape != aruco_shape) or (num != aruco_num):
#           chosen_shapes.append(shape)
#           chosen_nums.append(num)
#           break
#       continue
#     elif i == 0 # caso seja a primeira plataforma, cria o aruco
#       aruco_shape = shapes(random.randint(0,2))
#       aruco_num = num[chosen_factor-3]
#       chosen_shapes.append(aruco_shape)
#       chosen_nums.append('ArUco_marker')
#       continue
#     elif i == 6: # caso esteja na última plataforma e nenhuma anterior for válida, cria uma válida
#       chosen_shapes.apppend(aruco_shape)
#       chosen_nums.append(aruco_num)
#     else: # caso contrário, cria uma plataforma normal...
#       shape = shapes(random.randint(0,2))
#       num = nums(random.randint(0,2))
#       chosen_shapes.append(shape)
#       chosen_nums.append(num)
#       if (shape == aruco_shape) and (num == aruco_num): valid_platform = True # e verifica se a plataforma criada é válida para o aruco dado
#   
#   # "remove a plataforma de decolagem". Apenas garante que todas as listas tenham o mesmo comprimento
#   x_coords.pop(0)
#   y_coords.pop(0)
# 
#   # une todos os parâmetros em uma lista de tuplas
#   randomized.append(zip(indexes, x_coords, y_coords, chosen_shapes, chosen_nums))
# 
#   return randomized

#!/bin/bash