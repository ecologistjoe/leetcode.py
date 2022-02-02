# This code demonstrates why you shouldn't implement a C-style linked list in python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        Head = None
        
        carry = 0
        while l1 and l2:
            
            v1 = l1.val
            v2 = l2.val
            
            t = v1+v2+carry
            NEW = ListNode(t%10)
            if not Head:
                Head = NEW
            else:
                cur.next = NEW
            cur = NEW
                
            if t>=10:
                carry = 1
            else:
                carry =0

            l1 = l1.next
            l2 = l2.next

        rem= None
        if l1:
            rem = l1
        elif l2:
            rem = l2
            
        
        while rem:
            v = rem.val
            t = v+carry
            NEW = ListNode(t%10)
            cur.next = NEW
            cur = NEW
            if t>=10:
                carry = 1
            else:
                carry =0
                

            rem = rem.next

         
        if carry==1:
            cur.next = ListNode(carry)
        
            
            
        return Head
    
        
    
    