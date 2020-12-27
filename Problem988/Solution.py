"""
n := the number of characters/numbers present in the tree node
n-1 = n/(n/n-1)

Avg Runtime Complexity: O(n*logn) 
(Reasoning): T(n) = 2*T(n/2) + n
Worst Runtime Complexity: O(n^2)  
(Reasoning): T(n) = T(n-1) + n (other side of tree is empty)

Avg Space Complexity: O(n*logn)
Worst Space Complexity: O(n^2)

Runtime: 52 ms, faster than 34.30% of submissions
Memory Usage: 15.4 MB, less than 57.49% of submissions

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = ""

    def isLeaf(node: TreeNode) -> bool:
        return (node.left == None) and (node.right == None)

    def intToLetter(num: int) -> str:
        return str(chr(num + 97))

    def localDFS(self, node, temp_string):
        letter = Solution.intToLetter(node.val) # O(1)
        new_temp_string = letter + temp_string # O(n)
        if(Solution.isLeaf(node)): 
            if(self.ans == "" or new_temp_string < self.ans):
                self.ans = new_temp_string
        else:
            if node.left != None:
                Solution.localDFS(self, node.left, new_temp_string) # REC
            if node.right != None:
                Solution.localDFS(self, node.right, new_temp_string) # REC

    def smallestFromLeaf(self, root: TreeNode) -> str:
        if root == None:
            return ""  
        else:
            Solution.localDFS(self, root, "")
            return self.ans

