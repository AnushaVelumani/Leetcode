# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
            
    def isSymmetric(self, root):
        def symm(root1, root2):
            if not root1 and not root2: 
                return True
            elif not root1 or not root2: 
                return False
            return root1.val == root2.val and symm(root1.left, root2.right) and symm(root1.right, root2.left)
        return symm(root, root)
        
                    
            
       

s=Solution()
s.isSymmetric([1,2,2,3,4,4,3])
