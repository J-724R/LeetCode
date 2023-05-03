class Solution:
  def preorderTraversal(self, root: TreeNode) -> list[int]:
    def dfs(node):
      if not node: return
      
      ans.append(node.val)

      dfs(node.left)
      dfs(node.right)

      return   
  
    ans = []
    dfs(root)

    return ans