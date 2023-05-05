# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # return False if the root is None
    if root is None:
      return False
    # if it reaches to the end and the val is equal to targetSum, return True
    if root.left is None and root.right is None:
      return root.val == targetSum
    # otherwise, we traverse left node and right node with the new targetSum `targetSum - root.val`
    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)