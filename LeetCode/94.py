from tree_util import TreeNode, build_tree, print_tree
class Solution:
    def inorderTraversal(self, root):
        ans = []
        if root.left():
            return ans

# 測試
root = build_tree([1, "null", 2, 3])
print(root.val())

sol = Solution()
print(sol.inorderTraversal(root))
