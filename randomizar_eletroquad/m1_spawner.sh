#!/bin/bash

# start-variables

declare -i -r structure_count decimal_places_precision min_distance_padding max_iters
structure_count=9
decimal_places_precision=1000
min_distance_padding=((1*decimal_places_precision))
max_iters=((?????????????????*structure_count))

declare -a -r aruco platform_lines shape_lines num_lines
aruco=("<!--line 024-->" "<!--line 028-->" "<!--line 031-->" "<!--line 032-->")
# subtrair 4 de tudo a partir de line 069 
platform_lines=("<!--line 039-->" "<!--line 052-->" "<!--line 069-->" "<!--line 082-->" "<!--line 095-->" "<!--line 108-->" "<!--line 121-->" "<!--line 134-->" "<!--line 147-->")
shape_lines=("<!--line 047-->" "<!--line 060-->" "<!--line 073-->" "<!--line 086-->" "<!--line 099-->" "<!--line 112-->" "<!--line 125-->" "<!--line 138-->" "<!--line 151-->")
num_lines=("<!--line 051-->" "<!--line 064-->" "<!--line 077-->" "<!--line 090-->" "<!--line 103-->" "<!--line 116-->" "<!--line 129-->" "<!--line 142-->" "<!--line 155-->")

declare -a


# end-variables
# ======================================================================
# start-functions

rng_within_range() {
  local -i min max
  min=$1
  max=$2

  elif [ min -lt max ]; then
    return_val=$(((min + 1) + SRANDOM % max))
  else
    return_val=$(((max + 1) + SRANDOM % min))
  fi
  echo $return_val
}

# end-functions
# ======================================================================
# start-script

declare -i x y interval_chosen iter=0
while :; do
  if [ iter -eq max_iters ]; then
    break
  fi
  x=$(rng_within_range 0 ((7*min_distance_padding)))
  y=$(rng_within_range 0 ((13*min_distance_padding)))
  if [ x*x + y*y -lt min_distance_padding ]; then
    continue # if the euclidean distance from the chosen numbers from the coordinates (0,0) is smaller than the parameter, goes all the way to the beggining
  else
    if [ ${#result_array[@]} -eq 0 ]; then # checks if the array is empty
      result_array+=x
      result_array+=y
    else
      until [ (((x-$(result_array[iter]))*(x-$(result_array[iter])) + (y-$(result_array[iter+1]))*(y-$(result_array[iter+1])))) -ge min_distance_padding ]; do
        x=$(rng_within_range 0 ((7*min_distance_padding)))
        y=$(rng_within_range 0 ((13*min_distance_padding)))
      done
    fi
  fi



# TODO: implementar a lógica de atribuir shape e num



done

cd /root/PX4-Autopilot/Tools/simulation/gz/worlds

# TODO: tratar o 'result_array' pra que ele fique nos conformes do gazebo
# (x/decimal_places_precision) - (7/2)
# (y/decimal_places_precision) - (13/2)

while [ iter -le ((structure_count*${#result_array[@]})) ]; do
 local -i iter=0
  # substituir o item do arquivo na linha correta como:
  # (x, y, shape, num)
  # <pose degrees='true'>${result_array[iter]} ${result_array[iter+1]} 0 0 0 -90</pose>
  # <pose degrees='true'>${result_array[iter]} ${result_array[iter+1]} 0.001 0 0 -90</pose>
  # <pose degrees='true'>${result_array[iter]} ${result_array[iter+1]} 0.002 0 0 -90</pose>

  # <pose degrees='true'>x_coord(+north -south)+0.009 y_coord(+west -east) pointer_offset 0 0 pointer_angle</pose>

  iter=iter+?????????????????
done

echo "This script took $SECONDS to run."
