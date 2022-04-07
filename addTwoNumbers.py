"""
2. Add Two Numbers

You are given two non-empty linked lists,
representing two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        res = []
        add = False
        while l1 is not None or l2 is not None:

            if l1 is not None and l2 is not None:

                toAdd = l1.val + l2.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd = toAdd % 10
                    add = True
                else:
                    add = False
                res.append(toAdd)
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                toAdd = l1.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd = toAdd % 10
                    add = True
                else:
                    add = False
                res.append(toAdd)
                l1 = l1.next
            elif l2 is not None:
                toAdd = l2.val + (1 if add else 0)
                if toAdd > 9:
                    toAdd = toAdd % 10
                    add = True
                else:
                    add = False
                res.append(toAdd)
                l2 = l2.next
        if add:
            res.append(1)
        header = ListNode(res[len(res) - 1])
        if len(res) > 1:
            prev = header
            for i in range(len(res) - 2, -1, -1):
                prev = ListNode(res[i], prev)
            header = prev
        return header
