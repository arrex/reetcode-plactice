from typing import List


class Solution1:
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


class Solution2:
    """
    Intuition:
        Instead of trying to brute force all 3-digit numbers from the input, we
        can try scanning through all possible 3-digit numbers that are even (search
        space small enough -- 450 nums to be exact).

        We iterate through each candidate and see if we can form it with the input
        we have.

    Runtime:
        O(n) to count the frequency.

        O(450) ~ O(1) to scan each candidate.

        Overall, O(n) runtime.

    Memory:
        O(10) ~ O(1) for the frequency counter as there are only 10 possible digits.
    """

    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        res = 0
        for n in range(100, 1000, 2):
            d1, rem = divmod(n, 100)
            d2, d3 = divmod(rem, 10)
            res += freq[d1] > 0 and freq[d2] > (d1 == d2) and freq[d3] > (d1 == d3) + (d2 == d3)

        return res
