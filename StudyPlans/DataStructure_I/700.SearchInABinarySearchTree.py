# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
  
#Solution from DBabichev 
class Solution:
  def helper(self, root):
    if not root or root.val == self.val: 
        self.Found = root
        return root
    
    if root.val < self.val:
        return self.helper(root.right)
    
    if root.val > self.val:
        return self.helper(root.left)

  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    self.val = val
    self.Found = None
    self.helper(root)
    return self.Found
    

# From C++ hi-ravi response
class SolutionII:
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None or root.val == val: return root
    if root.val > val:
      return self.searchBST(root.left, val)
    return self.searchBST(root.right, val)
