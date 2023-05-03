# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        currentNode = root
        stack, res = [],[]
        while stack or currentNode:
            while currentNode is not None:
                stack.append(currentNode)
                currentNode = currentNode.left
                
            currentNode = stack.pop()
            res.append(currentNode.val)
            currentNode = currentNode.right

        return res