class Solution:
  def generate(numRows: int):
    pascal=[1]*numRows
    for i in range(numRows):
      pascal[i]=[1]*(i+1)
      for j in range(1,i):
        pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
    return pascal
  


