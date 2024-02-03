import matplotlib.pyplot as plt

# Function to insert the values of all the octants
def insert(x_values, y_values, x, y):
    x_values.append(x)
    y_values.append(y)
    x_values.append(-x)
    y_values.append(y)
    x_values.append(x)
    y_values.append(-y)
    x_values.append(-x)
    y_values.append(-y)
    x_values.append(y)
    y_values.append(x)
    x_values.append(-y)
    y_values.append(x)
    x_values.append(y)
    y_values.append(-x)
    x_values.append(-y)
    y_values.append(-x)


def draw_mid_point_circle(x1, y1):
    r = y1

    # Calculation of d0(initial value of decigion parametre)
    d = 1 - r
    x_values = []
    y_values = []

    x=x1
    y=y1
    insert(x_values, y_values, x, y)

    # Break the loop when the value of x is less than equal y so the we can reflect the points in different coordinates
    while x < y:
        if d>=0:
            # Calculating di+1 for +ve di
            d = d + 2*x + 5 - 2*y
            x = x + 1
            y = y - 1            
        else:
            # Calculating di+1 for -ve di
            d = d + 2*x + 3
            x = x + 1
            y = y
        insert(x_values, y_values, x, y)
    return x_values, y_values



x1 = int(input("Enter the Starting point of x: "))
y1 = int(input("Enter the Starting point of y: "))
x_values, y_values = draw_mid_point_circle(x1, y1)

# Plotting the line
plt.scatter(x_values, y_values)
plt.gca().set_aspect('equal')
plt.title('Mid Point Circle Algorithm')
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
