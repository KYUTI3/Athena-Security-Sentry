import numpy as np

# Below is a 1D Array (The dtype allows you to change how much size it takes, the standard is Int32 but you can change it to take up more or less space)
a = np.array([1,2,3], dtype = 'int16')

print(a)


# Below is a 2D Array
b = np.array([[9.0, 8.0, 7.0],[6.0,5.0,4.0]])

print(b)

# Prints number of dimensions (Depends on what array you called)
print(a.ndim)

#Prints the shape of the array you called
print(b.shape)

# Prints the data type of array called 
print(a.dtype)

# Prints the size of array called 
print(a.itemsize)

# Prints total size of array called 
print(a.size * a.itemsize)

# Or you can use
print(a.nbytes)

# Prints Array B item size (floats are naturally bigger than integers)
print(b.itemsize)

c = np.array([[1,2,3,4,5,6,7], [8, 9, 10, 11, 12, 13, 14, ]])

t