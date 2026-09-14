from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    Intuition:
        We can separate the linked list into 3 components: the prefix, the part we
        need to reverse, and the suffix.

        We start by finding the end node of the prefix. Then, we reverse the middle
        segment by storing a reference to the head and tail of the reversed list.
        Finally, we link it to the prefix and suffix.

    Runtime:
        O(n) as we process every node up to once.

    Memory:
        O(1).
    """

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # do nothing
        if not head or left == right:
            return head

        # create dummy node to deal w edge cases
        dummy = ListNode()
        dummy.next = head

        # mark node right before node in pos=left
        prefix = dummy
        for _ in range(left - 1):
            prefix = prefix.next

        seg = prefix.next

        # reverse nodes within left and right boundaries
        tmp, prev, curr = None, None, prefix.next
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        # link with prefix
        prefix.next = prev
        seg.next = tmp

        return dummy.next


class Solution2:
    """
    Intuition:
        Same as Solution 1, but we write the reversing logic differently.
        The observation is that the leftmost node in the segment we need to
        reverse will become the new tail. Thus, we simply process the node
        in its 'next' ptr and move it to the prefix to reverse.

        E.g.

        list = [1 2 3 4 5 6]
        left = 2
        right = 5

        The end of the prefix is at node 1.

        So nodes 2, 3, 4, 5 need to be reversed.

        After:
        - 1 iter -> [1 3 2 4 5 6]
        - 2 iters -> [1 4 3 2 5 6]
        - 3 iters -> [1 5 4 3 2 6]

    Runtime:
        O(n) as we process each node up to once.

    Memory:
        O(1).
    """

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # do nothing
        if not head or left == right:
            return head

        # create dummy node to deal w edge cases
        dummy = ListNode()
        dummy.next = head

        # mark node right before node in pos=left
        prefix = dummy
        for _ in range(left - 1):
            prefix = prefix.next

        seg = prefix.next

        # reverse nodes within left and right boundaries
        tmp, prev, curr = None, None, prefix.next
        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        # link with prefix
        prefix.next = prev
        seg.next = tmp

        return dummy.next
