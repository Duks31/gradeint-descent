import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def func1(x):
    return x**2-4*x+1

def gradient_func1(x):
    return 2*x-4

def func2(x):
    return x**4-2*x**3+3

def gradient_func2(x):
    return 4*x**3-6*x**2

def func3(x):
    return x**2 - 2*x + 3

def gradient_func3(x):
    return 2*x - 2

def gradient_descent(start, gradient_function, learning_rate, max_iterations, tolerance = 0.01):
    x = start
    steps = [x]
    
    for _ in range(max_iterations):
        gradient = gradient_function(x)
        x -= learning_rate * gradient
        steps.append(x)
        
        if abs(gradient) < tolerance:
            break
    
    return steps, x

history, result = gradient_descent(9, gradient_func1, 0.01, 100)

# print(history, result)

# Visualizing the gradient descent
x_vals = np.linspace(-10, 15, 400)
y_vals = func1(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label='Function: $f(x) = x^2 - 2x + 3$')
line, = ax.plot([], [], 'ro-', label='Gradient Descent Path')
min_point, = ax.plot([], [], 'go', label='Minimum')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Gradient Descent Visualization')
ax.legend()
ax.grid()
ax.set_xlim(-6, 10)
ax.set_ylim( -5, 60)

def init():
    line.set_data([], [])
    min_point.set_data([], [])
    return line, min_point

def animate(i):
    x = history[i]
    y = func1(x)
    line.set_data(history[:i+1], func1(np.array(history[:i+1])))
    min_point.set_data(x, y)
    return line, min_point

ani = FuncAnimation(fig, animate, frames=len(history), init_func=init, blit=True)

plt.show()

ani.save('grad_desc.gif')
