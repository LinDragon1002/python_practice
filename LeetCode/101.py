from tree_util import TreeNode, build_tree, print_tree
from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        return isMirror(root.left,root.right)
# 測試
root = build_tree([1,2,2,3,4,4,3])

sol = Solution()
print(sol.isSymmetric(root))
