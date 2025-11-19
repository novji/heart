import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Function to create the heart shape
def heart(x, y, scale):
    return (x**2 + (y * scale - np.sqrt(abs(x)))**2 - 1)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis("off")  # Hide axes for aesthetics

# Create a grid of x and y values
x = np.linspace(-2, 2, 400)
y = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x, y)

# Initial contour plot
scale = 1
contour = ax.contourf(X, Y, heart(X, Y, scale), levels=[-0.1, 0], colors='red')

# Function to update the plot for animation
def update(frame):
    global contour
    for c in contour.collections:
        c.remove()  # Remove old contours

    # Make the heart "beat" by changing its vertical scale
    scale = 1 + 0.1 * np.sin(frame / 10.0 * 2 * np.pi)
    contour = ax.contourf(X, Y, heart(X, Y, scale), levels=[-0.1, 0], colors='red')
    return contour.collections

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Display the animation
plt.show()
