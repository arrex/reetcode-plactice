from typing import List


class Solution:
    """
    Intuition:
        Brute force approach. We form all valid 3-digit numbers and
        check if each is distinct and even.

    Runtime:
        O(n^3) with our loops.

    Memory:
        O(n^3) for the hashset.
    """

    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        res = 0

        for i in range(len(digits)):
            if digits[i] == 0:
                continue

            for j in range(len(digits)):
                if j == i:
                    continue

                for k in range(len(digits)):
                    if k == j or k == i:
                        continue

                    n1, n2, n3 = digits[i], digits[j], digits[k]
                    num = n1 * 100 + n2 * 10 + n3

                    if num % 2 == 0 and num not in seen:
                        seen.add(num)
                        res += 1

        return res
