#!/usr/bin/python
# Import required libraries
import numpy as np

vector = [1, 2, 3]
matrix = [ [1, 2, 3, 4], 
           [5, 6, 7, 8],
           [9, 0, 1, 2] ]

def matrixTranspose(matrix):
    """
    Matrix Transpose function with interspersed print statements
    for explanatory purposes. We'll disect the following list comprehension :
    
    [ [row[n] for row in matrix] for n in range(len(matrix[0]))]
    
    """
    
#   Let's inspect which  matrix was provided as an argument? : 
#
#    [[1 2 3 4]
#     [5 6 7 8]
#     [9 0 1 2]]
#
    print 'Lets inspect which  matrix was provided as an argument? :'
    print np.matrix(matrix)
    
#   Now, let's disect the list comprehension which will transpose this
#   matrix. Start from the back when trying to understand what a list 
#   comprehension does. So we see that it tries the access the first 
#   row in the Matrix : [1 2 3 4]
    print 'matrix at row 0:'
    print matrix[0]
    
#   It does this to determine the number of columns the matrix has, as
#   each row will have an equal number of elements. 
    print 'length of Matrix at row 0'
    print len(matrix[0])

#   The number of columns is them used to create a 'range list' to 
#   iterate over : [0, 1, 2, 3]
    print 'The number of col in which will be used to create a range'
    print range(len(matrix[0]))

#   So in this particular case the list comprehension is simply:
#   [ [row[n] for row in matrix] for n in [0,1,2,3]]

#   The outer loop (the outer list comprehension) 'locks' the column
#   number for each full cycle of inner loop (inner list comprehension).

#   So in first instance 'n' is fixed at 0, and so when it executes the
#   inner loop :

#   [row[n] for row in matrix]

#  it goes through each row in the matrix and takes the nth element from the 
#  row. In the example, in the first cycle 'n' would be 0, and so the elements
#  taken from our examplary matrix would be [1,5,9]. These numbers are stored 
#  inside of a list (that's what list comprehensions do), and it will ask for 
#  the next value of 'n'. Now that 'n' is fixed as 1, it will go through a whole 
#  cycle again. Now it takes [2,6,0] from out examplary matrix. This continues 
#  for as long as there are more rows in the matrix.

    print 'Formatted as a matrix...'
    return [[row[n] for row in matrix] for n in range(len(matrix[0])) ]

#  Ultimately the function returns the transposed matrix : 
#
#   [[1 5 9]
#    [2 6 0]
#    [3 7 1]
#    [4 8 2]]
#


def vectorMatrixMultiplication(matrix,vector):
# make sure matrix col is as wild as vector length
    print 'In vectorMatrixMultiplication...'
    print 'matrix col:'
    print len(matrix[0])
    print 'matrix row:'
    print len(matrix)
    print 'vector length:'
    print len(vector)

    if len(matrix) == len(vector):
    	matrix = matrixTranspose(matrix)
    	print 'Need to transpose...'
    	print matrix


    return [row[0]*vector[0] + row[1]*vector[1] + row[2]*vector[2] for row in matrix]




print np.matrix(matrixTranspose(matrix)) # Formatted as a matrix

print vectorMatrixMultiplication(matrix,vector)


### EOF ###