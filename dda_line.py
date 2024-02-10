import matplotlib.pyplot as plt

def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        change = abs(dx)
    else:
        change = abs(dy)

    xinc = dx/change
    yinc = dy/change
    
    x_values = []
    y_values = []

    x=x1
    x_values.append(x)
    y=y1
    y_values.append(y)

    while x<x2 and y<y2:
        x=x+xinc
        x_values.append(round(x))
        y=y+yinc
        y_values.append(round(y))
    print("Coordinates for DDA")
    print(x_values)
    print(y_values)
    return x_values, y_values

import matplotlib.pyplot as plt

def draw_bresenhams_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    m = dy/dx
    p = (2*dy) - dx

    x_values = []
    y_values = []
    p_values =[]

    x=x1
    x_values.append(x)
    y=y1
    y_values.append(y)
    p_values.append(p)

    while x<x2 and y<y2:
        if m < 1 and p < 0:
            x = x + 1
            y = y
            p = p + 2*dy
        elif m < 1 and p >= 0:
            x = x + 1
            y = y + 1
            p = p + 2*dy - 2*dx
        elif m >= 1 and p < 0:
            x = x
            y = y + 1
            p = p + 2*dx
        elif m >= 1 and p >= 0:
            x = x +1
            y = y + 1
            p = p + 2*dx - 2*dy
        x_values.append(x)
        y_values.append(y)
        p_values.append(p)
    
    x=x2
    x_values.append(x)
    y=y2
    y_values.append(y)
    print("Coordinates for Bresenhams")

    print(x_values)
    print(y_values)
    return x_values, y_values


# x1 = int(input("Enter the Starting point of x (x1): "))
# y1 = int(input("Enter the Starting point of y (y1): "))
# x2 = int(input("Enter the end point of x (x2): "))
# y2 = int(input("Enter the end point of y (y2): "))
# x_values, y_values = draw_bresenhams_line(x1, y1, x2, y2)

# # Plotting the line
# # plt.plot(x_values, y_values, marker='o', linestyle='-', color = "red")
# # plt.title('Bresenhams Line Drawing Algorithm')
# # plt.axvline(x=0, c="black")
# # plt.axhline(y=0, c="black")
# # plt.xlabel('X-axis')
# # plt.ylabel('Y-axis')
# # plt.grid(True)

# x_values1, y_values1 = draw_line_dda(x1, y1, x2, y2)

# # Plotting the line
# plt.plot(x_values, y_values, marker='o', linestyle='-', color = "RED", linewidth=10)
# plt.plot(x_values1, y_values1, marker='o', linestyle='-')
# plt.axvline(x=0, c="black")
# plt.axhline(y=0, c="black")
# plt.title('Line Drawing Algorithm')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.grid(True)
# plt.show()