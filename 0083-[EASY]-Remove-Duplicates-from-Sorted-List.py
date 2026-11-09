# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        We use 2 pointers. `prev` anchors how much of the list we've
        processed while `curr` is used for exploration. We skip
        duplicates while moving `curr` and modify the link if there
        were any duplicates.

    Runtime:
        Each node is processed once so O(n).

    Memory:
        O(1) for the ptrs.
    """

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        prev, curr = None, head
        while curr:
            # move up
            prev, curr = curr, curr.next

            # skip all duplicates
            while curr and prev.val == curr.val:
                curr = curr.next

            # modify link
            prev.next = curr

        return head
