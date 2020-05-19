import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]

numbers = np.array([[0,5,10],[15,20,25],[50,75,100]])

result = numbers[:1,2]

print(result)