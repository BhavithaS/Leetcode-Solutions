# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root : return
        queue = [root.val]

        def trav(root) :
            if not root : return
            if root.left :
                queue.append(root.left.val)
                trav(root.left)
            if root.right :
                queue.append(root.right.val)
                trav(root.right)
        trav(root)

        res = []
        for i in range(len(queue)) :
            for j in range(len(queue)) :
                if i == j : continue
                else :
                    k = abs(queue[i]-queue[j])
                    if k not in res :
                        res.append(k)
        return min(res)
      
      
#approach - 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float('inf')
        self.prev = None

        def inorder(root) :
            if not root : return

            inorder(root.left)
            if self.prev is not None :
                self.ans = min(self.ans,root.val-self.prev)
            self.prev = root.val
            inorder(root.right)
        inorder(root)
        return self.ans
