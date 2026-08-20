from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    Intuition:
        Since we cannot index efficiently in a linked list, we map the linked list
        to an array to be able to access different indices efficiently. This way,
        we can pass through the array to compute all the twin sums are return the
        max.

    Runtime:
        O(n) -> dominated by traversal of input linked list.

    Memory:
        O(n) -> dominated by size of linked list.
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        sums = []

        for i in range(len(nums) // 2):
            sums.append(nums[i] + nums[-1 - i])

        return max(sums)


class Solution2:
    """
    Intuition:
        We are guaranteed that the linked list has an even number of
        elements. By reversing the 2nd half of the linked list, we can
        obtain 2 sublists that we can then traverse simultaneously to
        compute twin sums. This saves us from allocating extra space
        for an array.

    Runtime:
        O(n) to traverse the linked list and find its length.

    Memory:
        O(1) since we don't need to allocate any other data structure.
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        # Figure out the length of the list
        N = 0
        curr = head

        while curr:
            N += 1
            curr = curr.next

        # Reverse 2nd half
        curr = head

        for i in range(N // 2 - 1):
            curr = curr.next

        # Vars to reverse 2nd half of linked list
        rev_head, prev = curr.next, None
        # Break link between 1st and 2nd half
        curr.next = None

        while rev_head:
            tmp = rev_head
            rev_head = rev_head.next
            tmp.next = prev
            prev = tmp

        # Traverse 1st half and reverse 2nd half to find max twin sum
        res = 0
        l1, l2 = head, prev

        while l1:
            sum = l1.val + l2.val

            res = max(res, sum)

            l1 = l1.next
            l2 = l2.next

        return res
