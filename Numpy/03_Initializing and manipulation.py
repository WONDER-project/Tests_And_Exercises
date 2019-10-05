import numpy
import copy

# Array with all elements = 0

print(numpy.zeros((2, 3))) # prints a matrix with 2 rows, 3 columns, each element = 0

#_______________________________________________________________________________________________________________________

# Array with all elements = 1

print(numpy.ones((4, 2, 2), dtype='int')) # prints a matrix with dimensions 4x2x2, each element = 1

#_______________________________________________________________________________________________________________________

# Array where all elements are any number

print(numpy.full((2, 2), None)) # 1st parameter takes shape, 2nd parameter is value of all elements

#_______________________________________________________________________________________________________________________

# Array with same shape

a = numpy.array([[1, 2], [2, 3], [3, 4]])
print(numpy.full_like(a, 4)) # Generates an array filled with 4's, with the same shape as a

#_______________________________________________________________________________________________________________________

# Array where all elements are random decimal numbers

print(numpy.random.rand(4 ,2)) #argument is the shape

#_______________________________________________________________________________________________________________________

# Array where all elements are integers

print(numpy.random.randint(-4, 8, size=(3, 3))) # random integers between -4 and 8(exclusive) size is the shape of array

#_______________________________________________________________________________________________________________________

# Identity matrix

numpy.identity(5) #prints identity 5x5 matrix 

#_______________________________________________________________________________________________________________________

# Repeat an array

arr = numpy.array([[1, 2, 3]])
r1 = numpy.repeat(arr, 3, axis=0) # repeat the matrix arr 3 times, along the 0th axis (rows)
print(r1)

#_______________________________________________________________________________________________________________________

# Construct the following matrix:
#  1 1 1 1 1
#  1 0 0 0 1
#  1 0 9 0 1
#  1 0 0 0 1
#  1 1 1 1 1

output = numpy.ones((5, 5)) # initiate 5x5 matrix with all ones
print(output)

z = numpy.zeros((3, 3)) # initiate 3x3 matrix with all zeros
z[1, 1] = 9 # replace the central element of the zeros matrix with 9
print(z)

output[1:4,1:4] = z # replace the required region of output matrix with z
print(output)

iterable = copy.deepcopy(output)

#_______________________________________________________________________________________________________________________

# Copying

a = numpy.array([1,2,3])
b = a.copy() #simply using 'b = a' means 'a' and 'b' both point to the same thing, so any change in 'b' is also reflected in 'a'

b = copy.deepcopy(a)
b[0] = 100

print(a)
print(b)

#_______________________________________________________________________________________________________________________

# Iteration

a = numpy.arange(6).reshape(2,3) # .reshape changes array shape to 2 rows, 3 columns
print(a)
for x in numpy.nditer(a): #iterates over all values in the array
    print(x,'\n')

#_______________________________________________________________________________________________________________________

# Reversing an array

a = numpy.arange(8).reshape((2,2,2))
print(a)
a0=numpy.flip(a, 0) # reverses matrix a along 0 axis
print(a0)
a1=numpy.flip(a, 1) # reverses matrix a along 0 axis
print(a1)
a2=numpy.flip(a, 2) # reverses matrix a along 0 axis
print(a2)


# Iteration

for i in range(iterable.shape[0]):
    for j in range(iterable.shape[1]):
            print(iterable[i, j])

for j in range(iterable.shape[1]):
    for i in range(iterable.shape[0]):
            print(iterable[i, j])

for row in iterable:
    for element in row:
        print(element)
