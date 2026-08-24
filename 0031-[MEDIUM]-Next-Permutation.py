from typing import List


class Solution:
    """
    Intuition:
        The first insight is to notice that an array in decreasing order cannot
        have a lexicographically larger permutation.

        Take [3, 2, 1] for example. There is no possible permutation with these
        elmts that is larger.

        We can generalize this insight. For a given array, we search for its
        "suffix" that is in decreasing order.

        We have 3 major cases:

        If the suffix is only 1 elmt long, then we swap it with the second to
        last elmt (which is greater than it) to form the next permutation.

        If the suffix is the whole array, then there is no larger permutation.
        We return the smallest permutation by reversing the array into
        increasing order.

        If the suffix is between 1 and N, then the elmt previous to the left
        boundary will be our pivot. The invariant here is that the suffix
        is sorted is decreasing order. So we scan right to left and stop at
        the first elmt in the suffix that is greater than the pivot and swap
        them. After swapping, the suffix will still be in decreasing order,
        so we reverse it to yield the next valid smallest permutation.

    Runtime:
        O(n) to find the pivot using l, r ptrs.

        For the 3 subcases, the worst case scenario is having to reverse the
        whole array, so O(n).

        O(n) overall runtime complexity.

    Memory:
        O(1) for the l, r ptrs.
    """

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # base case
        if len(nums) == 1:
            return nums

        N = len(nums)
        r, l = N - 1, N - 1

        while l > 0 and nums[l - 1] >= nums[l]:
            l -= 1

        if r == l:
            # case sorted segment has only 1 elmt
            # swap last 2 elmts
            nums[-1], nums[-2] = nums[-2], nums[-1]
        elif r - l + 1 == N:
            # case whole array is in reverse order
            # i.e. no lexicographically larger permutation
            # return reversed array (incr order)
            nums.reverse()
        else:
            # case len of sorted segment k is somewhere in
            # between i.e. 1 < k < N
            # find elmt to swap with pivot
            pivot = l - 1

            # scan right to left and stop at first elmt
            # that is larger than pivot
            swap = r
            while nums[pivot] >= nums[swap]:
                swap -= 1
            nums[pivot], nums[swap] = nums[swap], nums[pivot]

            # reverse segment
            nums[l:] = reversed(nums[l:])
