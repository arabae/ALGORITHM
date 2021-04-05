# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = [root, root]
        while q:
            l = q.pop(0)
            r = q.pop(0)

            if not l and not r:
                continue

            if not l or not r:
                return False
            else:
                if l.val == r.val:
                    q.extend([l.left, r.right, l.right, r.left])
                else:
                    return False
        return True