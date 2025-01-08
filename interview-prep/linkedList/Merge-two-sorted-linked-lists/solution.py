# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None and list2 == None:
            return None
        l1_curr = list1
        l2_curr = list2
        head = None
        curr = None
        while l1_curr != None or l2_curr != None:
            if l1_curr == None:
                if head == None:
                    head = ListNode(val=l2_curr.val, next=None)
                    curr = head
                else:
                    curr.next = ListNode(val=l2_curr.val, next=None)
                    curr = curr.next
                l2_curr = l2_curr.next
                continue
            if l2_curr == None:
                if head == None:
                    head = ListNode(val=l1_curr.val, next=None)
                    curr = head
                else:
                    curr.next = ListNode(val=l1_curr.val, next=None)
                    curr = curr.next
                l1_curr = l1_curr.next
                continue
            #
            if l1_curr.val >= l2_curr.val:
                if head == None:
                    head = ListNode(val=l2_curr.val, next=None)
                    curr = head
                else:
                    curr.next = ListNode(val=l2_curr.val, next=None)
                    curr = curr.next
                l2_curr = l2_curr.next
                continue
            if head == None:
                head = ListNode(val=l1_curr.val, next=None)
                curr = head
            else:
                curr.next = ListNode(val=l1_curr.val, next=None)
                curr = curr.next
            l1_curr = l1_curr.next

        return head
