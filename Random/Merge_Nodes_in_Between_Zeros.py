# Definition for singly-linked list.
from typing import Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currnode = ListNode
        currnode = head.next
        sumnode = currnode
      
        while(currnode):
            sum = 0
            while(currnode.val != 0):
                    sum+= currnode.val
                    currnode = currnode.next
            sumnode.val = sum
            currnode = currnode.next
            sumnode.next = currnode
            sumnode = sumnode.next
                
        return head.next

    
                    
        
            
            
    

a = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(0,ListNode(1,ListNode(2,ListNode(0)))))))
b = ListNode
b = a.mergeNodes(head)
while(b):
    print(b.val)

