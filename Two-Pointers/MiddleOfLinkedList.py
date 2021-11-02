### Given the head of a singly Linked List. Return the middle node of the linked list
### If there are 2 middle nodes, return the 2nd middle node
# head = [1,2,3,4,5]
## Note: In Linked List, we usually use the head node(first node) to represent whole list


### Answer
## Use 2 pointers - fast and slow.
## Fast moves with 2 nodes at a time and slow moves 1 node at a time.
## So, when fast reaches the end, slow will be in the middle position

## Time = O(n/2) = O(n) [No constants, they are cut off of n/2 = n]

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
def middleOfLinkedList(head: ListNode) -> ListNode:
    # Initialize pointers to first node
    slow = fast = head
    # Checking if fast and fast.next exist
    # This is for handling case when list length is even, next will be null
    while fast and fast.next:
        # Fast pointer will move by 2 nodes
        fast = fast.next.next
        # Slow pointer will move by 1 node.
        # Slow will be at middle element when fast reaches the end
        slow = slow.next
    return slow
