from typing import List


class Solution:
    """
    Intuition:
        Add another loop on top of 3Sum solution to pick 4th
        elmt.

    Runtime:
        O(n log n) to sort.

        O(n^3) to find quadruplets with 3 loops; 2 for-loops,
        1 while-loop.

        Overall, O(n^3) dominates.

    Memory:
        Number of distinct quadruplets we can form is n^3, so
        at worst O(n^3) memory for 'res' array. This is because
        we have n choices for a, n choices for b, n choices for
        c. But once we have chosen the first 3 elmts, the fourth
        one becomes deterministic. This means we have n * n * n
        which gives n^3.

        Note that auxiliary memory usage is O(1).
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []

        for i in range(N):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 3sum
            target1 = target - nums[i]
            for j in range(i + 1, N):
                # skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # 2sum
                target2 = target1 - nums[j]
                l, r = j + 1, N - 1
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == target2:
                        a, b, c, d = nums[i], nums[j], nums[l], nums[r]
                        res.append((a, b, c, d))

                        # skip duplicates
                        while l < N and nums[l] == c:
                            l += 1

                        while r > j and nums[r] == d:
                            r -= 1
                    else:
                        if sum < target2:
                            l += 1
                        else:
                            r -= 1

        return res
