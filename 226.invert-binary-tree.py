# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertNode(node):
    if node is None:
        return None
    node.left, node.right = node.right, node.left
    invertNode(node.left)
    invertNode(node.right)
    return node

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invertNode(root)
