# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# Doesn't work with edge case of val being the last node of the list
class Solution:
  def removeElementsI(self, head, val):
    dummyHead = ListNode()
    current = dummyHead
    while head:
      if head.val != val:
        current.next = head
        current = current.next
      head = head.next
    
    return dummyHead.next
  
# TS recursive solution by mlajkin
function removeElements(head: ListNode | null, val: number): ListNode | null {
    if (head === null) return null
    if (head.val === val) return removeElements(head.next, val)
    return (head.next = removeElements(head.next, val), head) 
};

