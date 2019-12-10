''' Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image 90 degrees

image = [
          [1,2,3,4]      [1,1,1,1] 
          [1,2,3,4] turn [2 2 2 2] 
          [1,2,3,4]  to  [3 3 3 3] 
          [1,2,3,4]      [4,4,4,4] 
        ] 

Make a new Matrix storing the first element of each array in the original matrix as a row
'''
import numpy as np

matrix = [
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4],
          [1,2,3,4]
         ] 

def matrixRotation(matrix):
  newMatrix = np.zeros([4,4])
  i = 0
  for row in matrix:
    for pixel in range(len(row)):
      newMatrix[pixel,i] = row[pixel]
    i += 1 
  return newMatrix

print(matrixRotation(matrix))
