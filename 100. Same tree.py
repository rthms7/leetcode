# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #Logic: first check if p or q are both null which is a positive case. if not then traveres p and q trees recursively and create a list that represents the trees. if the lists are equal then the trees are the same.        
        if p==q:
            return True
        print(p)
        print(q)
        p_btree=traverse(p,[])
        q_btree=traverse(q,[])
        if p_btree==q_btree:
            return True
        else:
            return False

        # """

        # #alternate solution without need of traverse function. it checks conditions for inquality and returns False if any inequality. Otherwise if there is no inequality then the trees are same 
        
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # """

    
def traverse(p,btree=[]):
    if p:
        btree.append(p.val)
    else:
        return btree    #if tree is empty
    if (p.left is None) and (p.right is None):
        return btree    #child node
    if p.left is not None:
        traverse(p.left,btree)
    else:
        btree.append('null')    #add null to list if left node is missing
    if p.right:
        traverse(p.right,btree)
    return btree

        