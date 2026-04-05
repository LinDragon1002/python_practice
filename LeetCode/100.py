from tree_util import build_tree,TreeNode
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 兩個都是 None → 相同
        if not p and not q:
            return True
        # 只有一個是 None → 結構不同
        if not p or not q:
            return False
        # 值不同 → 不相同
        if p.val != q.val:
            return False
        # 遞迴比較左子樹和右子樹
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# 測試
p = build_tree([2,2,2,"null",2,"null","null",2])
q = build_tree([2,2,2,2,"null",2,"null"])

sol = Solution()
print(sol.isSameTree(p,q))
