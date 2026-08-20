from collections import defaultdict
from typing import List


class Solution:
    """
    Intuition:
        We create a hashmap to compute the frequence of each element in the input array. Then,
        we use a set to track the number of unique occurrences/frequencies. If we find a duplicate,
        we return false.

    Runtime:
        O(n). We need one pass to build the frequency hashmap and another to check if each
        frequency is unique.

    Memory:
        O(n) since we need to store a hashmap and a hashset.
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqs = defaultdict(int)

        for n in arr:
            freqs[n] += 1

        seen = set()

        for freq in freqs.values():
            if freq in seen:
                return False

            seen.add(freq)

        return True
