from typing import List


class Solution:
    """
    Intuition:
        Loop through all the numbers and count the number of 1 bits in the
        binary representation of each string.

    Runtime:
        O(n * log n) since we need to iterate through each number n, then need
        to compute the number of 1's in the binary representation of each number
        n.

    Memory:
        O(n) since we need to store the res array.

    Notes:
        This solution provides a "brute force" approach. We can definitely remove
        the log n factor out of the runtime complexity.
    """

    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            res.append((i).bit_count("1"))

        return res
