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


class Solution3:
    """
    Intuition:
        We can combine the intuitions of both previous solutions to form a third
        alternative.

        We can fine-tune the brute force approach from Solution 1 and combine it
        with the frequency counting idea from Solution 2.

        We count the frequency of each digit and store all even digits we encounter
        since the requirement is to form even 3-digit numbers.

        Then, we iterate through each distinct even digit we have found. We fix
        this even digit as the last digit in our number to make it even. This
        means that we need to find the 1st and 2nd digits.

        We subtract the even number we have affixed from our freq counter temporarily
        and go through every pair of digits to try and form numbers. Then, we also
        look at digits whose frequency is greater or eq to 2 so that we can use
        both digits.

    Runtime:
        O(n) to calculate the frequency counter.

        O(1) for the loops since there are 5 even digits for the outer loop, and each
        nested layer has up to 10 iterations.

        Overall, O(n) runtime.

    Memory:
        O(10) ~ O(1) for the frequency counter.

        O(5) ~ O(1) for the even digits set.

        Overall, O(1) memory.
    """

    def totalNumbers(self, digits: List[int]) -> int:
        freq = [0] * 10
        evens = set()
        for d in digits:
            freq[d] += 1
            if d % 2 == 0:
                evens.add(d)

        res = 0
        for e in evens:
            freq[e] -= 1

            for i in range(10):
                if freq[i] < 1:
                    continue

                for j in range(i + 1, 10):
                    if freq[j] < 1:
                        continue

                    # num = i j e
                    if i != 0:
                        res += 1
                    # num = j i e
                    if j != 0:
                        res += 1

            for i in range(1, 10):
                # num = i i e
                if freq[i] >= 2:
                    res += 1

            freq[e] += 1

        return res
