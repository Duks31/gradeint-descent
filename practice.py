import numpy as np
import matplotlib.pyplot as plt



# def normalize(n,list):
#     ''' Normalizes the values of the list between 0 and n'''
#     result = []
#     for i in list:
#         sigmoid = n / (n + i)
#         result.append(round(sigmoid, 2))
    
#     return result
    
# n = 10
# list = [i for i in range(1, 100)]
# result = normalize(n=n, list=list)

# for i in result:
#     if i == n:
#         print("The Function to mormalize is not working!!!")
#     break
# print("Worked all fine!!!")


# X = 2 * np.random.rand(100,1)
# y = 4 + 3 * X + np.random.randn(100,1)

# X_b = np.c_[np.ones((100, 1)), X]
# thetha_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# x_new = np.array([[0], [2]])
# x_new_b = np.c_[np.ones((2, 1)), x_new]

# y_predict = x_new_b.dot(thetha_best)
# print(y_predict)

# plt.plot(x_new, y_predict, "r-")
# plt.plot(X, y, "b.")
# plt.axis([0, 2, 0, 15])
# plt.show()

# print(x_new_b)
# plt.plot(X,y,"b.")
# plt.show()