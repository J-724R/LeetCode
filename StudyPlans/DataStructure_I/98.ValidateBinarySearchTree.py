# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node: return True
            if not low < node.val < high: return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, -float("inf"), float("inf"))
    
# Iterative solution
class SolutionII:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
    Q = [[root,float("-inf"),float("inf")]]

    while Q:
      node, lower, upper  = Q.pop()
    
      validNode = lower < node.val < upper
      if not validNode:
          return False
      
      if node.left:
          Q.append([node.left,lower,node.val])
      if node.right:
          Q.append([node.right,node.val,upper])

    return True