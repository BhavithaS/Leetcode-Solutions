# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root) :
        if root == [] : return []
        res = []
        def tree(root,res) :
            if root is None : return
            res.append(root.val)
            tree(root.left,res)
            tree(root.right,res)

        tree(root,res)
        return res

