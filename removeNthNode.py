"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findSize(self, header):
        temp = header
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def removeNthFromEnd(self, header, n):
        size = self.findSize(header)
        prev = header
        next = header.next
        i = 0
        if next == None:
            header = None
            return header
        if size - n - 1 == -1:
            header = next
            return header
        while next != None:
            if i == size - n - 1:
                print(prev.val)
                print(next.val)
                prev.next = next.next
                break
            prev = next
            next = next.next
            i += 1
        return header
