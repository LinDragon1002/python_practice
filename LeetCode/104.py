from tree_util import TreeNode, build_tree, print_tree
class Solution:
    def inorderTraversal(self, root):
        def dfs(n,node,tot):
            if not node:
                return max(n,tot)
            tot = dfs(n+1,node.left,tot)
            tot = dfs(n+1,node.right,tot)
            return tot
        return dfs(0,root,0)

# 測試
root = build_tree([3,"null",7])


sol = Solution()
print(sol.inorderTraversal(root))
