# Stats & Probability: Mean, Variance, Normal Distribution, Simulations
#
# - np.mean(nums): Mean (average) of a list/array
# - np.var(nums): Variance (spread) of a list/array
# - np.random.normal(loc, scale, size): Generate samples from a normal distribution
# - random.choice(list): Randomly select an item from a list
# - random.randint(a, b): Random integer between a and b (inclusive)

import numpy as np
import random

# Mean and Variance
nums: list = [1, 2, 3, 4, 5]
print("Mean:", np.mean(nums))  # Compute mean
print("Variance:", np.var(nums))  # Compute variance

# Normal Distribution
samples: np.ndarray = np.random.normal(loc=0, scale=1, size=5)  # 5 samples from N(0,1)
print("Normal distribution samples:", samples)

# Simulate Coin Toss
coin_tosses: list = [random.choice(["H", "T"]) for _ in range(10)]  # 10 random tosses
print("Coin tosses:", coin_tosses)

# Simulate Dice Rolls
dice_rolls: list = [random.randint(1, 6) for _ in range(10)]  # 10 random dice rolls
print("Dice rolls:", dice_rolls)
