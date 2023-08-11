import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

current_position1 = (0.7, 0.4, z_function(0.7, 0.4))
current_position2= (0.3, 0.8, z_function(0.3, 0.8))
current_position3 = (-0.5, 0.4, z_function(-0.5, 0.4))
learning_rate = 0.01

fig = plt.figure()
ax = plt.subplot(projection="3d", computed_zorder=False)

# for i in range(100):
#     X_derivitive, Y_derivitive = calculate_gradient(current_position[0], current_position[1])
#     X_new, Y_new = current_position[0] - learning_rate * X_derivitive, current_position[1] - learning_rate * Y_derivitive
#     Z_new = z_function(X_new, Y_new)
#     current_position = (X_new, Y_new, Z_new)

#     ax.plot_surface(X, Y, Z, cmap='viridis', zorder = 0)
#     ax.scatter(current_position[0], current_position[1], current_position[2], color='red', zorder=1)
#     plt.pause(0.01)
#     ax.clear()

def update(frame):
    global current_position1
    global current_position2
    global current_position3
    
    X_derivative, Y_derivative = calculate_gradient(current_position1[0], current_position1[1])
    X_new = current_position1[0] - learning_rate * X_derivative
    Y_new = current_position1[1] - learning_rate * Y_derivative
    Z_new = z_function(X_new, Y_new)
    current_position1 = (X_new, Y_new, Z_new)

    X_derivative, Y_derivative = calculate_gradient(current_position2[0], current_position2[1])
    X_new = current_position2[0] - learning_rate * X_derivative
    Y_new = current_position2[1] - learning_rate * Y_derivative
    Z_new = z_function(X_new, Y_new)
    current_position2 = (X_new, Y_new, Z_new)

    X_derivative, Y_derivative = calculate_gradient(current_position3[0], current_position3[1])
    X_new = current_position3[0] - learning_rate * X_derivative
    Y_new = current_position3[1] - learning_rate * Y_derivative
    Z_new = z_function(X_new, Y_new)
    current_position3 = (X_new, Y_new, Z_new)

    ax.clear()
    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0)
    ax.scatter(current_position1[0], current_position1[1], current_position1[2], color='red', zorder=1)
    ax.scatter(current_position2[0], current_position2[1], current_position2[2], color='magenta', zorder=1)
    ax.scatter(current_position3[0], current_position3[1], current_position3[2], color='cyan', zorder=1)

ani = FuncAnimation(fig, update, frames=100, repeat=False)

# Save the animation as a GIF
ani.save('optimization_animation.gif', writer='pillow')

plt.show()