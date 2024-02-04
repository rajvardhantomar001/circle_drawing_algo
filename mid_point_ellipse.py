import matplotlib.pyplot as plt

# Function to insert the values of all the regions in the ellipse
def insert(x_values, y_values, x, y):
    x_values.append(x)
    y_values.append(y)
    x_values.append(-x)
    y_values.append(y)
    x_values.append(x)
    y_values.append(-y)
    x_values.append(-x)
    y_values.append(-y)


def draw_mid_point_ellipse(a, b):
    x = 0
    y = b
    x_values = []
    y_values = []

    # Region 1
    d = pow(b, 2) - (pow(a, 2) * b) + (0.25 * pow(a, 2))
    insert(x_values, y_values, x, y)

    # Region 1
    while (pow(a, 2) * (y - 0.5)) > (pow(b, 2) * (x + 1)):
        if d < 0:
            d = d + pow(b, 2) * (2 * x + 3)
        else:
            d = d + (pow(b, 2) * (2 * x + 3)) + (pow(a, 2) * (-2 * y + 2))
            y = y - 1
        x += 1
        insert(x_values, y_values, x, y)

    # Region 2
    d2 = (pow(b, 2) * (x + 0.5) * (x + 0.5)) + (pow(a, 2) * (y - 1) * (y - 1)) - (pow(a, 2) * pow(b, 2))
    while y > 0:
        if d2 < 0:
            d2 += pow(b, 2) * (2 * x + 2) + pow(a, 2) * (-2 * y + 3)
            x += 1
        else:
            d2 += pow(a, 2) * (-2 * y + 3)
        y -= 1
        insert(x_values, y_values, x, y)

    return x_values, y_values


a = int(input("Enter the semi-major axis (a): "))
b = int(input("Enter the semi-minor axis (b): "))
x_values, y_values = draw_mid_point_ellipse(a, b)
n = len(x_values)
# Plotting the ellipse
plt.scatter(x_values, y_values)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
for i in range (0, n):
    plt.plot(x_values[i], y_values[i])

plt.gca().set_aspect('equal')
plt.title('Mid Point Ellipse Algorithm')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
