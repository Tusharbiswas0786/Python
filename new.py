#zero array method

import numpy as np
zero_array1 = np.zeros(((1,3,3))) #3d
zero_array2 = np.zeros((2,3)) #2d
zero_array3 = np.zeros(3,) #1d

print (zero_array1)
print (zero_array2)
print (zero_array3)

#one array method

one_array1 = np.ones(((1,3,3))) #3d
one_array2 = np.ones((2,3)) #2d
one_array3 = np.ones(3,) #1d

print (one_array1)
print (one_array2)
print (one_array3)

#full array method

Full_array1 = np.full((3,) , 2) #1d #Inside bracket we need to give shape 1st and then which element we want in array
Full_array2 = np.full(((2,3)) , 2) #2d
Full_array3 = np.full(((1,3,3)) , 2) #3d

print (Full_array1)
print (Full_array2)
print (Full_array3)

#Identity matrix - all elements zero except diagonal elements. It must be 3x3 matrix

id_matrix = np.eye(3) #3d

print (id_matrix)

#Empty array

print(np.empty(2)) #It generates random 2 values

#Evenly spaced array - It starts with 1st element and giving 2 2 gaps till reaching 10 but not include the last element.

print (np.arange(1,10,2)) 

#Specify no of equally spaced values between a range

print(np.linspace(1,10,4))

#Random values array - float

r_array = np.random.rand(3,2)

print(r_array)

#Random values array - Int

rint_array = np.random.randint(1,20,(3,2)) #1st element is starting element, second is last element and 3rd is the dimention of array which we need to print

print(rint_array)


