# Using the same code from last problem (102)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return 0
    queue, result = deque([root]), []
    
    while queue:
      level = []
      for i in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
      result.append(level)
    return len(result) 
  
# Another solution from c++ code

def levelOrderII(self, root: Optional[TreeNode]) -> List[List[int]]:
  if root == None: return 0
  left = levelOrderII(root.left)
  right = levelOrderII(root.right) 
  return max(left, right) + 1;