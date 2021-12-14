# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # root를 보고, low보다 작으면 오른쪽만 탐색, high보다 크면 왼쪽만 탐색, 같으면 양쪽 다 탐색
        # 그 다음 root도 마찬가지로 탐색하면서, low를 만나면 오른쪽만 탐색하고, 종료 high를 만나면 왼쪽만 탐색하고 종료
        q = [root]
        value_sum = 0
        while q:
            root_node = q.pop()
            if root_node:
                if low <= root_node.val <= high:
                    value_sum += root_node.val
                
                if root_node.val <= low:
                    q.append(root_node.right)
                elif root_node.val >= high:
                    q.append(root_node.left)
                else:
                    q.append(root_node.right)
                    q.append(root_node.left)
                    
        return value_sum
