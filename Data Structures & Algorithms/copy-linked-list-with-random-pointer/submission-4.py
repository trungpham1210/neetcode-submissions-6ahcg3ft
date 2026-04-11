"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        #interweaving
        l1 = head
        while l1 is not None:
            l2 = Node(l1.val) #create without any link
            l2.next = l1.next #link the next value of the copy to the next original value
            l1.next = l2 #link the orginal value to the copy value
            l1 = l2.next #move the pointer to the next orginal value

        newHead = head.next #keep this so we can just return the chain later without having to find it again
        #assign random
        l1 = head
        while l1 is not None: 
            if l1.random is not None:
                #match the random of the copy value to its random value
                l1.next.random = l1.random.next #l1.next (l2)'s random will be the next value of l1'srandom 
            l1 = l1.next.next #move the pointer so we can continue
        #untangle, separated the copy list
        l1 = head
        while l1 is not None: 
            l2 = l1.next
            l1.next = l2.next
            if l2.next is not None:
                l2.next = l2.next.next # this is incase l2.next is None
            l1 = l1.next #link the original list 
        
        return newHead
