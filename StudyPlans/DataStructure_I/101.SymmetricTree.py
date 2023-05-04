# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def helper(left, right):
  if left == None or right == None : 
    return left == right
  if left.val == right.val:
    return helper(left.left, right.right) and helper(left.right, right.left)
  else:
    return False
  
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    return root==None or helper(root.left, root.right)