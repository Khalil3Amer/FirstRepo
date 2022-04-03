"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = list2
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            list2 = list2.next
        current = ListNode(head.val)
        head = current
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        if list1 == None:
            current.next = list2
        else:
            current.next = list1
        return head
