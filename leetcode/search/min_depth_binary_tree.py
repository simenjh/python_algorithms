# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        current_min_depth = -1
        def recurser(node, depth):
            nonlocal current_min_depth
            if(node.left == None and node.right == None):
                if(current_min_depth < 0):
                    current_min_depth = depth
                elif(depth < current_min_depth):
                    current_min_depth = depth
            else:
                if(node.left):
                    recurser(node.left, depth+1)
                if(node.right):
                    recurser(node.right, depth+1)
        recurser(root, 1)
        return current_min_depth
    
