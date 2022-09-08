import numpy as np
import pandas as pd

# Task 1: Create a DataFrame
# Create a 3x4 numpy array, each cell populated with a random integer.
# Do the following:
#
# Create an 3x4 (3 rows x 4 columns) pandas DataFrame in which the columns are named Eleanor, Chidi, Tahani, and Jason. Populate each of the 12 cells in the DataFrame with a random integer between 0 and 100, inclusive.
#
# Output the following:
#
# the entire DataFrame
# the value in the cell of row #1 of the Eleanor column
# Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason
my_data = np.random.randint(low=0, high=101, size=(3, 4))

# my solution
data = np.array([100*np.random.random(4), 100*np.random.random(4), 100*np.random.random(4)]).astype(int)
column_names = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
dataFrame = pd.DataFrame(data=data, columns=column_names)

print(data)
print(dataFrame)

print("\n row 1 of the eleanor: %d\n"%dataFrame['Eleanor'][1])
dataFrame['Janet'] = dataFrame['Tahani']+dataFrame['Jason']