from typing import List, Deque
from collections import deque

"""

Problem 102: Binary Tree Level Order Traversal (Medium)

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

   3
9   20
   15 7

Approach: Using a recursive fn and two queues for the current level and next
level, you can gradually add a node's value to their level's corresponding list.
If a node has children, append them to next level queue. If the current level
queue is nonempty, pop from this queue and recurse on this. If the next level
queue is nonempty but this level is, increment level index, pop from next level
queue, and recurse. If both are empty, return the accumulative solution.


N := Number of nodes in tree
Runtime Complexity: O(N)
Space Complexity: O(N)
Runtime: 76ms, faster than 5.35%
Memory: 15.7MB, less than 8.66%

"""
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        soln = []
        return Solution.levelOrder_tr(root, 0, deque(), deque(), soln)

    def levelOrder_tr(node:TreeNode, level:int, this_level:Deque[TreeNode], next_level:Deque[TreeNode], accum:List[List[int]]) -> List[List[int]]:
        if node is not None:
            if level == len(accum):
                accum.append([])
            children = [node.left, node.right]
            for child in children:
                if child is not None:
                    next_level.append(child)
            accum[level].append(node.val)

            if len(this_level) > 0:
                next_node = this_level.popleft()
                return Solution.levelOrder_tr(next_node, level, this_level, next_level, accum)
            elif len(this_level) == 0 and len(next_level) > 0:
                next_node = next_level.popleft()
                return Solution.levelOrder_tr(next_node, level+1, next_level, deque(), accum)
            else:
                return accum
        else:
            return accum

if __name__ == '__main__':
    solver = Solution()

    # first test
    lt = TreeNode(9, None, None)
    rt = TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))
    t = TreeNode(3, lt, rt)
    print(solver.levelOrder(t))

    # second test
    t = TreeNode(1, None, None)
    print(solver.levelOrder(t))

    # third test
    t = None
    print(solver.levelOrder(t))

    # fourth test
    l4t = TreeNode(20, None, None)
    l3t = TreeNode(17, None, l4t)
    l2t = TreeNode(10, None, l3t)
    t = TreeNode(0, None, l2t)
    print(solver.levelOrder(t))
