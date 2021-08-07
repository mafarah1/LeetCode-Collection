"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q=deque()
    
        if root is None:
            return []
        
        result=[]
        q.append(root)
        
        while q:
            level=[]
            size=len(q)
            while size:
                curr_node=q.popleft()
                level.append(curr_node.val)
                for child in curr_node.children:
                    q.append(child)
                size-=1
            result.append(level)
            
        return result
        
        # q = deque()
        # q.append(root)
        # curr_node = q.popleft()
        # print(curr_node.val)
        