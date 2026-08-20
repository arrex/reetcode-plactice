from typing import List


class Solution1:
    """
    Intuition:
        We can think of the input as intervals or groups for which every
        elmt within a given group can jump to the same "local maxima".

        These groups are delimited by smaller values to the left and larger
        values to the right (inverse of jump rules!). Effectively, every
        elmt in the res array is the max of itself and all consecutive
        larger elmts immediately to its left.

        We use a monotonic stack (bottom = lowest, top = highest) to solve
        this problem. We push new blocks onto the stack and merge them
        if the topmost block has a value larger than our current block
        (meaning we can jump to it).

    Runtime:
        O(n) as we loop through every elmt. At each step, we push once and
        pop at most once which leads to O(1) cost. Overall runtime stays
        linear at O(n).

    Memory:
        In the worst case, each elmt forms a block in the stack (e.g.
        sorted input array), so need up to O(n) space.
    """

    def maxValue(self, nums: List[int]) -> List[int]:
        N = len(nums)
        stack = []  # block = (value, left, right)

        for i in range(N):
            currVal = nums[i]
            currLeft = i
            currRight = i

            # merge logic
            while stack and stack[-1][0] > nums[i]:
                topVal, topLeft, _ = stack.pop()
                currVal = max(currVal, topVal)
                currLeft = topLeft

            stack.append((currVal, currLeft, currRight))

        res = [0] * N
        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                res[j] = stack[i][0]

        return res


class Solution2:
    """
    Intuition:
        Use a 2 pass approach. We can populate "naive" values in the result
        using prefix max scan.

        Then, our 2nd scan replicates the "merging" we did in the monotonic
        stack approach. We maintain a dynamic index 'ix' while traversing the
        'res' array backwards. At each step, we can either inherit values by
        seeing that we can jump to a smaller value or we can adjust 'ix' by
        realizing that we have encountered a smaller value which marks the
        transition to a different block interval.

    Runtime:
        Still O(n) since 2 linear scans.

    Memory:
        Still O(n) for 'res' array. O(1) auxiliary space.
    """

    def maxValue(self, nums: List[int]) -> List[int]:
        # pass 1 - prefix max for each elmt
        N, res = len(nums), [nums[0]]
        for n in nums[1:]:
            res.append(max(res[-1], n))

        # pass 2 - adjust maximum values
        ix = N - 1
        for i in range(N - 2, -1, -1):
            # prefix max can jump to lower value
            # lower value at nums[ix] must jump to value greater or eq
            if res[i] > nums[ix]:
                res[i] = res[ix]
            # smaller value encountered, break through to diff interval
            # this diff interval has diff max value than curr interval so adjust bounds
            if nums[i] < nums[ix]:
                ix = i
        return res
