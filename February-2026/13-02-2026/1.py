#create array from 1 - 10 and only print even numbers
import numpy as np
arr=np.arange(1,11)
print(arr[arr%2==0])