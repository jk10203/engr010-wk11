#my module
# <li>A function that generates a plot, given a function name and the range of x values</li>
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(func, x_values):
    y_values = func(x_values)
    #func.__name__ to get function name
    plt.plot(x_values, y_values, 'b-', label=func.__name__)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f"Plot of {func.__name__}")
    plt.legend()
    plt.grid(True)
    plt.show()


# <li>The Chooser class from the OOP lecture</li>
import random

class Chooser:
    def __init__(self, items):
        if not items:
            raise ValueError("Item list cant be empty.")
        self.items = list(items)  #store as list so we can index 
    
    def choose(self):
        return random.choice(self.items)


    # <li>Your solution to either a Project Euclid or Leetcode problem</li>
def two_sum(nums, target):
    seen = {}  #maps number -> index
    for i, num in enumerate(nums):
        diff = target - num #complement
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return None  #in case there's no valid pair
