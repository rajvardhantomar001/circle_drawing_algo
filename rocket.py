from DDA_algo_line import DDA_line_drawing
import functions
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

fig, ax = plt.subplots()

DDA_line_drawing(10,0,10,100,ax)
DDA_line_drawing(40,0,40,100,ax)
DDA_line_drawing(40,20,50,10,ax)
DDA_line_drawing(40,40,50,30,ax)
DDA_line_drawing(50,10,50,30,ax)
DDA_line_drawing(55,10,55,30,ax)
DDA_line_drawing(10,20,0,10,ax)
DDA_line_drawing(10,40,0,30,ax)
DDA_line_drawing(0,10,0,30,ax)
DDA_line_drawing(-5,10,-5,30,ax)
DDA_line_drawing(10,100,25,155,ax)
DDA_line_drawing(40,100,25,155,ax)
DDA_line_drawing(30,0,30,-30,ax)
DDA_line_drawing(20,0,20,-30,ax)
# DDA_line_drawing(15,160,32,160,ax)
# DDA_line_drawing(32,160,50,150,ax)
# DDA_line_drawing(50,150,32,160,ax)
# DDA_line_drawing(32,160,25,180,ax)

a = Ellipse((12.5,50), 15, 5, fc = 'black')
b = Ellipse((12.5,0), 15, 5, fc = 'black')
c = Ellipse((12.5,-15), 5, 3, fc = 'black')
d = Ellipse((12.5,30), 5, 20, fc = 'blue')
e = Ellipse((-1,5), 2.5, 1, fc = 'black')
f = Ellipse((-1,15), 2.5, 1, fc = 'black')
g = Ellipse((26,5), 2.5, 1, fc = 'black')
h = Ellipse((26,15), 2.5, 1, fc = 'black')


ax.add_patch(a)
ax.add_patch(b)
ax.add_patch(c)
ax.add_patch(d)
ax.add_patch(e)
ax.add_patch(f)
ax.add_patch(g)
ax.add_patch(h)


# top = [
#     (10,50), (100,0), (100,75), (25,75), (25,0)
# ]

# chimni_coordinates = [
#     (25,75), (100, 75), (100, 100), (12, 100), (25, 75)
# ]

# window_coordinates = [
#     (12, 100), (0, 75), (25, 75), (12, 100)
# ]

# door_coordinates = [
#     (0, 0), (25, 0), (25, 0), (25, 75), (0, 75), (0, 0)
# ]

# # Extract x and y coordinates for filling the area
# x_coords = [point[0] for point in hut_coordinates]
# y_coords = [point[1] for point in hut_coordinates]

# x_coords_chim = [point[0] for point in chimni_coordinates]
# y_coords_chim = [point[1] for point in chimni_coordinates]

# x_coords_window = [point[0] for point in window_coordinates]
# y_coords_window = [point[1] for point in window_coordinates]

# x_coords_door = [point[0] for point in door_coordinates]
# y_coords_door = [point[1] for point in door_coordinates]

# # Fill the area enclosed by the lines (coloring the hut)
# ax.fill(x_coords, y_coords, color='orange') 
# ax.fill(x_coords_chim, y_coords_chim, color='red')  
# ax.fill(x_coords_window, y_coords_window, color='yellow')
# ax.fill(x_coords_door, y_coords_door, color='brown')

# '''Normal Plot'''
plt.show()

# '''Translated Plot'''
# dx= int(input("Enter the translation on x-axis:"))
# dy = int(input("Enter the translation on y-axis:"))
# functions.translate_graph(ax, dx=dx, dy=dy)
# ax.set_title('Translated Graph')
# plt.show()

# '''Rotation Plot'''
# deg = int(input("Enter the degree of rotation:"))
# functions.rotate_graph(ax, angle_degrees=deg)
# ax.set_title('Rotated Graph')
# plt.show()

# '''Shear Plot'''
# dx= int(input("Enter the Shear factor on x-axis:"))
# dy = int(input("Enter the Shear factor on y-axis:"))
# functions.shear_graph(ax, shear_factor_x = dx, shear_factor_y = dy)
# ax.set_title('Shear Graph')
# plt.show()

# '''Reflection Plot'''
# dx= (input("Enter the Reflection axis:"))
# functions.reflect_graph(ax, reflection_axis = dx)
# ax.set_title('Reflection Graph')
# plt.show()
