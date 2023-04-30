# C++ Solution
class Solution:
    def searchMatrix(matrix,target):
        x = 0 
        y = 0
        def isValid(x, y):
            if (x < 0 or x == len(matrix)): 
                return False;
            if (y < 0 or y == len(matrix[0])): 
                return False;
            return True;
        while (isValid(x, y)):
            if (matrix[x][y] == target): return True;
            if (x < len(matrix) - 1): 
                if (matrix[x + 1][y] <= target):
                    x += 1; 
                    continue;
            y += 1;
        return False;

# Binary search
class Solution:
    def searchMatrix(matrix, target):
        n = len(matrix);
        m = len(matrix[0]);
        i = 0;
        j = m-1;
        while(i < n and j >= 0):
            mid = (i + j) >> 1;
            if(matrix[i][j] == target):
                return True;
            elif(matrix[i][j] < target):
                i += 1;
            else:
                j -= 1;
        return False;