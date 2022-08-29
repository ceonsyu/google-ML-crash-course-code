import numpy as np

# Task 1: Create a Linear Dataset
feature = np.arange(6,21)
print(feature)
label = 3*feature+4
print(label)

#Task 2: Add Some Noise to the Dataset
noise = 4*np.random.random(15)-2
print(noise)
label = label+noise
print(label)
