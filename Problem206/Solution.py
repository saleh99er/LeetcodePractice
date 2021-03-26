"""
Problem 206: Reverse Linked List

Problem: Given the head of a singly linked list, reverse the list, and return
the reversed list.

Solution: Window approach where prev, curr, next = null, head, null and your
window gets curr's next pointer for next. curr's next pointer is set to prev,
prev is set to curr, and curr is set to next. Window continues left to right
until curr is null. 

n := number of nodes in list
Runtime complexity: O(n)
Space complexity: O(1)
Runtime: 36 ms, faster than 66.46%
Memory Usage: 15.5 MB, less than 93.24%

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "%s, %s" % (str(self.val), str(self.next))
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

if __name__ == '__main__':
    solver = Solution()
    t1 = ListNode('a',ListNode('b',ListNode('c')))
    output = solver.reverseList(t1)
    assert str(output) == 'c, b, a, None'

    t2 = None
    output = solver.reverseList(t2)
    assert str(output) == 'None'

    t3 = ListNode('z')
    output = solver.reverseList(t3)
    assert str(output) == 'z, None'

    t4 = ListNode('a',ListNode('b',ListNode('c', ListNode('d', ListNode('e')))))
    output = solver.reverseList(t4)
    assert str(output) == 'e, d, c, b, a, None'

    print("passed set test cases")
        