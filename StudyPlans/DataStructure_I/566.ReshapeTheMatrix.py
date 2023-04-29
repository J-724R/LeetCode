# Brute Force Solution
  #check if the new shape has the same number of elements
  #Create matrix
  #Traverse matrix and asing values to the new shape

class Solution:
    def matrixReshape(self, mat, r, c):
      m, n = len(mat), len(mat[0])
      if m * n != r * c:
          return mat
      
      new_mat = [[0] * c for _ in range(r)]
      
      index = 0
      for i in range(r):
          for j in range(c):
              row, col = divmod(index, n)
              new_mat[i][j] = mat[row][col]
              index += 1
              
      return new_mat   