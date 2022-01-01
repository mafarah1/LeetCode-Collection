# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_to_list(root: Optional[TreeNode], arr: list):
    if not root:
        return arr

    tree_to_list(root.left, arr)
    arr.append(root.val)
    tree_to_list(root.right, arr)

    return arr

class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        # BFS
        # Put every node in a hashmap,
        # If at any point the value is available, return both
        
        arr1 = []
        
        arr2 = tree_to_list(root,arr1)
        
        # Starting index of a2
        start = 0

        # Ending index of a2
        end = len(arr2) - 1

        while start < end:

            # If target found
            if arr2[start] + arr2[end] == target:
                return True

            # Decrements end
            if arr2[start] + arr2[end] > target:
                end -= 1

            # Increments start
            if arr2[start] + arr2[end] < target:
                start += 1
        
        return False