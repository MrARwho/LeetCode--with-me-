# Definition for singly-linked list.
from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = deque()
        temp = ListNode(0)
        sum = 0
        currnode = head
        temp = head
        
        while currnode != None:
            # if (currnode.val == 0 and len(a)>0):
            #     while (len(a)>0):
            #         sum+=a.pop()
            #     currnode.val = sum
            #     sum = 0
            #     temp.next = currnode
            if (currnode.val != 0):
                sum+=currnode.val()
                temp.next = currnode.next()
            else :
                temp.val = sum
                temp2 = ListNode(0)
                temp.next = temp2
            
            
    

a = Solution()
head = ListNode(0,ListNode(3,ListNode(1,ListNode(0))))
a.mergeNodes(head)
