from typing import List


class Solution:
    """
    Intuition:
        Maintain a hash set. If we have a collision, then we know we
        encountered a duplicate.

    Runtime:
        O(n).

    Memory:
        O(n).
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


class Solution2:
    """
    Intuition:
        Cheese solution, but did you know that the cost of len() for
        built-in data structures in Python is O(1)? :)

    Runtime:
        O(1).

    Memory:
        O(1).
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
