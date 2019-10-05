import numpy

a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

print("\nex 1")
print(a)

# Select a specific element from array as [row,column]
print("\nex 2")
print(a[1, 5]) # gets 5th column of 1th row (indexing starts from 0)

#_______________________________________________________________________________________________________________________

# Get all elements of a specific row
print("\nex 3")
print(a[0, :]) # Gives all columns in row 0, ':' is the basic slice syntax

#_______________________________________________________________________________________________________________________

# Get all elements of a specific columns
print("\nex 4")
print(a[:, 2]) # Gives every element in column 2

#_______________________________________________________________________________________________________________________

# Selecting with a step size
print("\nex 5")
print(a[0, 2:6:2]) # selects elements between the start(1) and end(5) indices, with step size 2. Note that start index
                  # is included but end index is not.

#_______________________________________________________________________________________________________________________

# Replacement of data
print("\nex 6")
a[1, 5] = 20 # repalce 1th element in 5th column with 20
a[:, 2] = [1, 2] #replaces the two elements of the 2th column with 1 and 2
print(a)
#_______________________________________________________________________________________________________________________

# 3d example of data replacement
print("\nex 7")
b = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b.shape)

print(b[0, 1, 1]) # Get specific element in 3d array, working from outside in

b[:, 1, :] = [[9, 9], [8, 8]] #replaces all elements in 1th row of all columns according to shape
print(b)


# last element

a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a[-1])
print(a[::2])
print(a[::-1])
print(a[::-2][::-1])
#_______________________________________________________________________________________________________________________
