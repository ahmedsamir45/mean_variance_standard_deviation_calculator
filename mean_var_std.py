import numpy as np
def calculate(list):
  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")

  x_array = np.array(list)
  x_array = x_array.reshape((3,3)) 

  # rows 
  row1 = x_array[0,:]
  row2 = x_array[1,:]
  row3 = x_array[2,:]

  # columns
  col1 = x_array[:,0]
  col2 = x_array[:,1]
  col3 = x_array[:,2]

  calculations = {
    'mean': [
      [col1.mean(), col2.mean(), col3.mean()],
      [row1.mean(), row2.mean(), row3.mean()],
      x_array.mean()
    ],
    'variance': [
      [col1.var(), col2.var(), col3.var()],
      [row1.var(), row2.var(), row3.var()],
      x_array.var()
    ],
    'standard deviation': [
      [col1.std(), col2.std(), col3.std()],
      [row1.std(), row2.std(), row3.std()],
      x_array.std()
    ],
    'max': [
      [col1.max(), col2.max(), col3.max()],
      [row1.max(), row2.max(), row3.max()],
      x_array.max()
    ],
    'min': [
      [col1.min(), col2.min(), col3.min()],
      [row1.min(), row2.min(), row3.min()],
      x_array.min()
    ],
    'sum': [
      [col1.sum(), col2.sum(), col3.sum()],
      [row1.sum(), row2.sum(), row3.sum()],
      x_array.sum()
    ]
  }

   

  return calculations

x = [0,1,2,3,4,5,6,7,8]
print(calculate(x))