import numpy
# numpy any

A = numpy.random.rand(4, 2)
print(A)
if numpy.any(A < 0.6): # if any element of the array is less than 0.6, prints 'match'
    print('match')

#_______________________________________________________________________________________________________________________

# numpy all

A = numpy.random.rand(4, 2)
print(A)
if numpy.all(A < 1.0): # if all elements of the array are less than 1, prints 'match'
    print('match')

#_______________________________________________________________________________________________________________________

# numpy where

a = numpy.array([[0, 1, 2],[0, 2, 4],[0, 3, 6]])
print(a)
print(numpy.where(a < 4, 0, 1)) # checks if any element in the array is less than 4, if not, sets to 1, else sets to 0
                                 # 1st argument is the condition, 2nd argument is the value when the condition is
                                 # is true, 3rd argument is the value when condition is false

#_______________________________________________________________________________________________________________________

# numpy logical and

a = numpy.arange(5)
print(a)
print(numpy.logical_and(a > 1, a < 4)) # gives the truth value of the intersection (logical and) of the two conditions,
                                       # for every element in the array

#_______________________________________________________________________________________________________________________

# numpy logical or

a = numpy.arange(5)
print(a)
print(numpy.logical_or(a < 1, a > 3)) # gives the truth value of the union (logical and) of the two conditions,
                                       # for every element in the array

#_______________________________________________________________________________________________________________________
A = numpy.random.rand(4, 2)
print(A)
if numpy.any(numpy.logical_and(A > 0.1, A < 0.6)): # if any element of the array is less than 0.6, prints 'match'
    print('match')

A = numpy.random.rand(4, 2)
print(A)
if numpy.all(numpy.logical_and(A > 0.5, A < 1.0)): # if all elements of the array are less than 1, prints 'match'
    print('match')


a = numpy.array([[0, 1, 2], [0, 2, 4], [0, 3, 6]])
print(a)
cursor = numpy.where(numpy.logical_and(a > 1, a < 4))

print(a[cursor])

import time


array = numpy.arange(0.1, 1003.5, 0.001)

t0 = time.time()
subarray = array[numpy.where(numpy.logical_or(numpy.logical_and(array > 10, array < 20),
                                              numpy.logical_and(array > 900, array < 950)))]

t1 = time.time() - t0
print("execute in ", t1, "seconds")

# traditional

array = array.tolist()
result = []

t0 = time.time()
for i in range(len(array)):
    value = array[i]

    if (value > 10 and value < 20) or (value > 900 and value < 950):
        result.append(value)

t2 = time.time() - t0
print("execute in ", t2, "seconds")
print("performance reduced by a factor: ", t2/t1)



