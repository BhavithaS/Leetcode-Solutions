# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return None

        res = [[root.val]]
        q = [root]
        flag = 0
        while q :
            queue = []
            child = []
            for i in q :
                
                if i.left :
                    child.append(i.left.val)
                    queue.append(i.left)
                if i.right :
                    child.append(i.right.val)
                    queue.append(i.right)
            q = queue
            if flag == 0 and child != []:
                res.append(child[::-1])
                flag = 1
            elif flag == 1 and child != []:
                res.append(child)
                flag = 0
        return res

#Approach-2        
