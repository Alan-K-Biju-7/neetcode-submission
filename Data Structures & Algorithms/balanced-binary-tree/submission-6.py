# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return False
            left = height(node.left)
            right = height(node.right)
            if  abs(left - right) > 1:
                self.balanced = False
               

            return 1 + max(left,right)
        self.balanced = True    
        height(root)
        
        return self.balanced
                
        
       


            
        