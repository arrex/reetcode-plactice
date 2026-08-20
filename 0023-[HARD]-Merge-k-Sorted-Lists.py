from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        This problem builds upon problem 21. We can reuse the same idea of merging 2 lists at a time
        to reduce the number of lists we have to merge by half at each iteration. We just need to
        implement some extra logic to account for an even and odd number of lists to merge.

        The bulk of the algorithm rests upon merging a given linked list with its subsequent neighbour
        in the array. If the array contains an odd number of linked lists, then the last one does not
        get merged with anything, hence the None argument.

    Runtime:
        O(N log K) where N is the total number of nodes and K is the number of linked lists in the
        input array. Merging 2 linked lists takes O(N) in the worst case since we have to traverse
        each node of all input linked lists and we reduce the number of lists to be merged by half
        at each iteration as mentionned previously which gives a log K scaling.

    Memory:
        O(1) auxiliary space since we only every manipulate the next pointers of existing nodes. No
        other data structure is used and we don't allocate any extra memory in our solution.
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    l1, l2 = lists[i], None
                    merged.append(self.mergeTwoLists(l1, l2))
                else:
                    l1, l2 = lists[i], lists[i + 1]
                    merged.append(self.mergeTwoLists(l1, l2))

            lists = merged

        return lists[0] if lists else None

    # Helper function
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next

        return dummy.next
