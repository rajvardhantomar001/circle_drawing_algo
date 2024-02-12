import math
import tkinter as tk

# Constants
WIDTH, HEIGHT = 400, 400
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
OUTER_CIRCLE_RADIUS = 100
INNER_CIRCLE_RADIUS = 20
ROTATION_SPEED = 1  # Adjust the rotation speed here

# Create a Tkinter window
root = tk.Tk()
root.title("Rotate Circle")

# Create a Canvas widget to draw on
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

angle = 0

def update_circle_position():
    global angle
    canvas.delete("inner_circle")  # Clear the previous inner circle

    # Calculate the position of the inner circle
    inner_circle_x = CENTER_X + OUTER_CIRCLE_RADIUS * math.cos(math.radians(angle))
    inner_circle_y = CENTER_Y + OUTER_CIRCLE_RADIUS * math.sin(math.radians(angle))

    # Draw the outer circle
    canvas.create_oval(CENTER_X + OUTER_CIRCLE_RADIUS, CENTER_Y + OUTER_CIRCLE_RADIUS,
                       CENTER_X - OUTER_CIRCLE_RADIUS, CENTER_Y - OUTER_CIRCLE_RADIUS, outline='black')

    # Draw the rotating inner circle
    canvas.create_oval(inner_circle_x + INNER_CIRCLE_RADIUS, inner_circle_y + INNER_CIRCLE_RADIUS,
                       inner_circle_x - INNER_CIRCLE_RADIUS, inner_circle_y - INNER_CIRCLE_RADIUS,
                       outline='black', fill='black', tags="inner_circle")

    angle += ROTATION_SPEED
    root.after(10, update_circle_position)  # Update the position every 20 milliseconds

update_circle_position()

root.mainloop()