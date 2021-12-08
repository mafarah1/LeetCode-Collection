# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preOrder(root, array):
    if root != None:
        array.append(root.val)
        preOrder(root.left, array)
        preOrder(root.right, array)
    return array

def tilt(root):
    
    if root != None:
        # First subtract
        root.val = abs(int(0 if root.left is None else sum(preOrder(root.left, []))) - int(0 if root.right is None else sum(preOrder(root.right, [])))) # -_- I was trying to call for root.left.val when it was None
        # I also missed a paranthesis placement
        
        if root.left != None:        
            # Then recur on left child
            tilt(root.left)
 
        if root.right != None:
            # Finally recur on right child
            tilt(root.right)

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        array = []
                
        tilt(root)
        
        preOrder(root, array)
        
        return sum(array)