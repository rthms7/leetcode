# Intuition
#<!--For my first approach, I decided to go with ordered dictionary where the keys were the individual elements and their values were their levels in the tree. This approach was limited because ordered dict could not support duplicate keys for duplicate elements. for my second solution to handle duplicates I flipped the keys and values to be the level and list of elements at that level. All test cases passed. time and space complexity can be optimised further -->

# Approach
#<!-- Common solution is to use collections.deque(double ended queue).queue length is checked while q still has elements. if q has elements it is popped from the left. if popped element is node its left and right attributes are appended to q, while its value is added to list. In every iteration of while loop all elements at a single level from left to right are appended to result -->

# Complexity
#- Time complexity: O(N)


#- Space complexity: O(N)


# Code
#```python []

import collections

'''
best solution
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque()
        q.append(root)
        print(len(q))
        while q:
            #queue length is checked while q still has elements. if q has elements it is popped from the left. if popped element is node its left and right attributes are appended to q, while its value is added to list. In every iteration of while loop all elements at a single level from left to right are appended to result 
            length = len(q)     
            #print(q)
            #print(length)
            level = []          
            for i in range(length):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


'''
for my second solution to handle duplicates I flipped the keys and values to be the level and list of elements at that level. All test cases passed.
'''
'''

from collections import OrderedDict
class TreeNode(object):
# Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #print(type(root))
        #print(root)
        tree = OrderedDict()
        level = 0
        final_tree,final_level = traverse(root,level,tree)
        #print(final_tree)
        final_tree = list_tree(final_tree)
        return final_tree
        #print(final_tree) 
       
def traverse(p,level,btree):
    if p:
        try:    #if key is not present then use exception handling to add the key
            btree[level].append(p.val)
        except KeyError:
            btree[level] = [p.val]
    else:
        return {},0    #if tree is empty
    if (p.left is None) and (p.right is None):
        return btree, level-1    #no child node
    if p.left is not None:
        btree, level = traverse(p.left,level+1,btree)
    if p.right:
        btree, level = traverse(p.right,level+1,btree)
    return btree, level-1

def list_tree(btree):
    final = [value for value in btree.values()]
    return final

def main():
    root = TreeNode(val = 3, left = TreeNode(val= 9, left= None, right= None), right= TreeNode(val= 20, left= TreeNode(val= 15, left= None, right= None), right= TreeNode(val= 7, left= None, right= None)))
    tree = OrderedDict()
    level = 0
    final_tree,final_level = traverse(root,level,tree)
    #print(final_tree)
    final_tree = list_tree(final_tree)
    print(final_tree)
    #sol = Solution()
    #sol.levelOrder(root=None)


main()

'''


'''
for my first approach, I decided to go with ordered dictionary where the keys were the individual elements and their values were their levels in the tree. This approach was limited because ordered dict could not support duplicate keys for duplicate elements
'''
'''
from collections import OrderedDict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #print(type(root))
        #print(root)
        tree = OrderedDict()
        level = 0
        final_tree,final_level = traverse(root,level,tree)
        #print(final_tree)
        final_tree = list_tree(final_tree)
        return final_tree
        #print(final_tree)

def traverse(p,level,btree):
    if p:
        btree[p.val] = level
    else:
        return {},0    #if tree is empty
    if (p.left is None) and (p.right is None):
        return btree, level-1    #child node
    if p.left is not None:
        btree, level = traverse(p.left,level+1,btree)
    if p.right:
        btree, level = traverse(p.right,level+1,btree)
    return btree, level-1

def list_tree(btree):
    final = list()
    print(btree)
    for item in btree.items():
        #print(item)
        key = item[0]
        value = item[1]
        try:
            if type(final[value]) is list:
                final[value].append(key)
        except IndexError:
            final.append(list())
            final[value].append(key)
    return final
'''