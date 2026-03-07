import random
import nump as np

general_z_offset = 0.001
padding = 2

sphere = [x_coord, y_coord, 1.7]
poles_and_cables = [
  ((x_coord, y_coord), (x_coord, y_coord), cable),
  ((x_coord, y_coord), (x_coord, y_coord), cable)
]

points = []

# comprimento do cabo = np.sin((points[i]-points[i-1])/2)*2*4.5