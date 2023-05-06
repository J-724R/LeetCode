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
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        while root:
            if root.val > large:  # p, q belong to the left subtree
                root = root.left
            elif root.val < small:  # p, q belong to the right subtree
                root = root.right
            else:  # Now, small <= root.val <= large -> This is the LCA between p and q
                return root
        return None



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