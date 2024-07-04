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
        temp = ListNode()
        sum = 0
        currnode = head
        
        while currnode != None:
            if (currnode.val == 0 and len(a)>0):
                while (len(a)>0):
                    sum+=a.pop()
                currnode.val = sum
                sum = 0
                temp = currnode
                
            
            
    

a = Solution()
head = ListNode(0,ListNode(3,ListNode(1,ListNode(0))))
a.mergeNodes(head)
