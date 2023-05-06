# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# There are only 3 posible scenarios
#   - 1 both values are smaller than root
#   - 2 both values are bigger than root 
  # - 3 one value is greater than the root and the other is smaler

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      right = max(p.val, q.val)
      left = min(p.val, q.val)
      if root.val < left:
          return self.lowestCommonAncestor(root.right, p, q)
      elif root.val > right:
          return self.lowestCommonAncestor(root.left, p, q)
      else:
          return root





# Very straight foward C++ Solution
# class Solution {
# public:
#     TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
#         if (p->val < root->val && q->val < root->val)
#             return lowestCommonAncestor(root->left, p, q);
#         else if (p->val > root->val && q->val > root->val)
#             return lowestCommonAncestor(root->right, p, q);
#         else return root;
#     }
# };     