from collections import defaultdict
from typing import List


class Solution1:
    """
    Intuition:
        Anagrams have the property where the frequency of their letters
        are identical. We just need to hash that property somehow. One
        way to achieve this is to compute the frequency of each letter
        as an array. We then cast that array to a tuple since dictionaries
        in Python require the key to be immutable.

    Runtime:
        O(N * K) where N is the length of the input array strs and K is
        the length of the longest string present in the array.

    Memory:
        O(N * K) with similar reasonning to runtime.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            key = [0] * 26

            for c in s:
                key[ord(c) - ord("a")] += 1

            map[tuple(key)].append(s)

        return list(map.values())


class Solution2:
    """
    Intuition:
        Instead of hashing frequency, we can also leverage the fact
        that anagrams have the same frequency by encoding a special
        string. We will essentially sort the string and use that as
        our key.

    Runtime:
        O(N * K * log K) -> Similar reasonning as Solution1's runtime,
        but we have an extra log K factor due to the sorting.

    Memory:
        Still O(N * K).

    Note:
        In theory, this solution is slower, but in practice it performs
        consistenly better than Solution1 because it leverages more
        built-in functions.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            map[key].append(s)

        return list(map.values())

        map = defaultdict(list)
