# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:23:34 2024

@author: Larrot
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x, x0, k):
    """
    Sigmoid function to smoothly transition between two values.
    
    Parameters:
        x (float): Input value.
        x0 (float): Midpoint of the sigmoid curve.
        k (float): Steepness of the curve.
    
    Returns:
        float: Smoothly interpolated value.
    """
    return 1 / (1 + np.exp(-k * (x - x0)))

def S_ALPHA(x):
    y2 = 0.01
    y1 = 0.0001
    transition_point = -12  # Adjust this point to control where the transition occurs
    # transition_point = 10**(-1)  # Adjust this point to control where the transition occurs
    steepness = 10  # Adjust this parameter to control the steepness of the transition
    
    return y1 + (y2 - y1) * sigmoid(x, transition_point, steepness)



# x_values = np.linspace(-19, 1, 100)
# y_values = [S_ALPHA(x_values[i]) for i in range(100)]

# # Plot the sigmoid function


# plt.plot(x_values, y_values)
# plt.title(r'Коэффициент $\alpha$ в зависимости от степени ионизации')
# plt.xlabel('X')
# plt.ylabel(r'$\alpha$')
# # plt.xlim(0, 10**(-15))
# plt.ylim(0.5*10**(-4), 2*10**(-2))

# # plt.xscale('log')
# plt.yscale('log')

# plt.grid(True)
# plt.legend()
# plt.show()