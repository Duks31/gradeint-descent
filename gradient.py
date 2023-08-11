import numpy as np 
import matplotlib.pyplot as plt

def func(x):
    return x ** 2

def func_derv(x):
    return 2 * x

x = np.arange(-100, 100, 0.1)
y = func(x)

current_position = (80, func(80))

learning_rate = 0.1

for _ in range(10):
    new_x = current_position[0] - learning_rate * func_derv(current_position[0])
    new_y = func(new_x)
    current_position = (new_x, new_y)

    plt.plot(x, y)
    plt.scatter(current_position[0], current_position[1], color = 'red')
    plt.pause(0.001)
    # plt.clf()

