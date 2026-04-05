from tree_util import TreeNode, build_tree, print_tree
class Solution:
    def inorderTraversal(self, root):
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans

# 測試
root = build_tree([1, "null", 2, 3])
print(root.val())

sol = Solution()
print(sol.inorderTraversal(root))
