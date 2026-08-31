from math import inf
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Intuition:
        We scan the linked list by looking at sets of 3 nodes (prev, curr, next) to
        find all the local maxima and minima. We record each critical point's position.

        Then, the maximum distance is simply the distance between the leftmost and
        rightmost critical points.

        And the minimum distance is the smallest distance between adjacent critical
        points.

    Runtime:
        O(n) to find the positions of all critical points.

        O(1) to compute max distance.

        We have at most O(n // 2) critical points, meaning finding the min distance
        takes O(n // 2) ~ O(n) time.

        Overall, O(n) runtime.

    Memory:
        O(n // 2) ~ O(n) to store all the positions of all the critical points.
    """

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # base case
        if not head:
            return [-1, -1]

        pos = 1
        crit = []
        prev, curr = head, head.next

        while curr and curr.next:
            next = curr.next

            if curr.val < prev.val and curr.val < next.val:
                crit.append(pos)

            if curr.val > prev.val and curr.val > next.val:
                crit.append(pos)

            prev, curr = curr, next
            pos += 1

        # base case
        if len(crit) < 2:
            return [-1, -1]

        maxDist = crit[-1] - crit[0]

        # check all adj pairs of crit pts
        minDist = inf
        for l in range(len(crit) - 1):
            r = l + 1
            minDist = min(minDist, crit[r] - crit[l])

        return [minDist, maxDist]
