# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        s, root_sum = [root], 0
        while s:
            x = s.pop()
            if x.left:
                x.left.val += (x.val * 10)
                s.append(x.left)
            if x.right:
                x.right.val += (x.val * 10)
                s.append(x.right)

            if not x.left and not x.right:
                root_sum += x.val

        return root_sum