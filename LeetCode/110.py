from tree_util import build_tree
class Solution:
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return 0, True
            
            left_h, left_bal = dfs(node.left)
            right_h, right_bal = dfs(node.right)

            is_balanced = is_balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
            height = max(left_h, right_h) + 1

            return height , is_balanced
        _, is_balanced = dfs(root)
        return is_balanced

# 測試
root = build_tree([3,9,20,None,None,15,7])


sol = Solution()
print(sol.inorderTraversal(root))


"""
[3,9,20,None,None,15,7]
[1,2,2,3,3,None,None,4,4]
"""

# 另解
"""
is_balanced = True
def post_order(root):
    nonlocal is_balanced
    if not root:
        return 0
    if not is_balanced:
        return 0
    left = post_order(root.left)
    right = post_order(root.right)
    if abs(left - right) > 1:
        is_balanced = False
        return 0

    return max(left, right) + 1

post_order(root)
return is_balanced
"""