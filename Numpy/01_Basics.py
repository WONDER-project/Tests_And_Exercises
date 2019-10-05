import numpy

# Initialize a numpy array from a python list
print("\nex 1")
a = numpy.array([1, 2, 3], dtype='int') #dtype='int32' assigns a 32 bit data type to the array. Strictly optional
print(a)

#_______________________________________________________________________________________________________________________

# Initialize a 2D numpy array from a list of 2 lists
print("\nex 2")
b = numpy.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]]) #floats are used as elements instead of int
print(b)
print(b.shape)

#_______________________________________________________________________________________________________________________

# Get dimension of array
print("\nex 3")
a = numpy.array([1, 2, 3])
b = numpy.array([[9.0, 8.0, 7.0],
                 [6.0, 5.0, 4.0]])

print(len(a))
print(len(b))
print(len(b[0]))

# NOPE: this is number of dimensions
print(a.ndim)
print(b.ndim)

#_______________________________________________________________________________________________________________________

# Shape of array
print("\nex 4")
b = numpy.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b.shape) #prints the shape of array b

#_______________________________________________________________________________________________________________________

# Type of array
print("\nex 5")
a = numpy.array([1,2,3])
b = numpy.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(a.dtype) #prints the type of array a, which is int32
print(b.dtype) #prints the type of array b, which is float64. By default, floats are bigger than integers.

print(type(a))
print(isinstance(a, numpy.ndarray))
#_______________________________________________________________________________________________________________________

# Size of array
print("\nex 6")
b = numpy.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b.size) #the number of elements in the array

#_______________________________________________________________________________________________________________________
