class Solution:
    """
    Intuition:
        Brute force approach using a fixed sliding window. We process
        each subarray and maintain a hashmap to count frequencies.

    Runtime:
        O(n * k) since we process each elmt in the input list `nums`
        and we also have a nested loop that iterates through the
        entire window of size k.

    Memory:
        O(n) for the `counter` hashmap.
    """

    def largestInteger(self, nums: list[int], k: int) -> int:
        counter = {}
        l, r = 0, k - 1

        while r < len(nums):
            # keep a set to avoid double counting the same elmt
            # consider nums = [2, 2], k = 2
            elmts = set()

            for i in range(l, r + 1):
                n = nums[i]
                elmts.add(n)

            for e in elmts:
                if e not in counter:
                    counter[e] = 0

                counter[e] += 1

            l += 1
            r += 1

        # find res
        res = -1
        for n, freq in counter.items():
            if freq == 1 and n > res:
                res = n

        return res
