# @leet start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def findLCA(tree, p, q):
    if not tree: return None
    if tree.val == p.val or tree.val == q.val: return tree
    if p.val < tree.val and q.val > tree.val: return tree
    if p.val > tree.val and q.val < tree.val: return tree
    if p.val < tree.val and q.val < tree.val:
        return findLCA(tree.left, p, q)
    else:
        return findLCA(tree.right, p, q)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return findLCA(root, p, q)
