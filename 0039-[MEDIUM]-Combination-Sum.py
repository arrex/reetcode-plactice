from typing import List


class Solution1:
    """
    Intuition:
        We use a brute-force DFS approach to solve this problem. At each step, we
        try to add every number in nums to our current combination. If the sum of
        the current combination equals target, we add it to our result set. If the
        sum exceeds target, we backtrack.

    Runtime:
        Let n be the length of nums, t be the target value, and m be the minimum
        value in nums.

        In the worst case, we can have a combination of length t/m. At each step,
        we have n choices (the numbers in nums). Therefore, the time complexity
        is O(n^(t/m)) since we have n branches at each recursive step and the
        depth is at most t/m.

    Memory:
        The call stack takes O(h) where h is the height of the recursion tree. We
        mentioneed this value to be t/m previously, so the overall memory complexity
        is O(t/m).
    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()

        # currently chosen, current sum, nums we can choose from
        def dfs(currNums, currSum):
            if currSum == target:
                currNums.sort()
                currNums = tuple(currNums)

                if currNums not in res:
                    res.add(currNums)

                return
            elif currSum > target:
                return

            # try with every single num
            for n in nums:
                copy = currNums.copy() + [n]
                dfs(copy, currSum + n)

        dfs([], 0)
        return [list(elmt) for elmt in res]


class Solution2:
    """
    Intuition:
        We can introduce 3 optimizations.

        The first optimization is to sort the nums array. This allows us to
        terminate early if the number at the current index exceeds the target.

        The second optimization is in managing the construction of our combinations.
        Instead of having to sort each combination to check uniqueness, we use
        a starting index to indicate which number we start building our current
        combinations from. This way, we ensure that each combination is sorted
        by default.

        Lastly, instead of trying every single element in nums, we reduce our
        choices to 2 options:
        - Add the number at the current start index to our current combination.
        - Skip it and move onto the next number by incrementing the start index.

    Runtime:
        Our longest combination can be of length t/m where t is target.

        At each recursive step, we are presented with 2 options. Given that the
        longest combination is of length target, the time complexity is O(2^(t/m)).

        This is better than O(n^(t/m)) from Solution1 since we reduced n choices to
        2.

    Memory:
        The call stack takes O(h) where h is the height of the recursion tree.
        In the worst case, we can have a combination of length t/m. Therefore,
        the overall memory complexity is O(t/m).
    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(startIx, currNums, currSum):
            if currSum == target:
                res.append(currNums)
                return
            elif currSum > target or startIx >= len(nums) or nums[startIx] > target:
                return

            # add num at startIx
            dfs(startIx, currNums + [nums[startIx]], currSum + nums[startIx])
            # move onto next num
            dfs(startIx + 1, currNums, currSum)

        dfs(0, [], 0)
        return res


class Solution3:
    """
    Intuition:
        We introduce 2 more optimizations.

        Instead of building a new list at each recursive step, we can modify
        the current list in place by appending and popping elements.

        The second optimization lies in the branching strategy. Rather than
        treating each recursion as a binary choice (take or skip), we loop
        through all valid candidates starting from the current index. This
        eliminates redundant recursive calls and leverages the sorted `nums`
        array to terminate early when the remaining target cannot be reached.

        Example redundant call:
            nums = [2, 3, 4]

            We want to build the combination [2, 4]

            Using Solution2, we would need a recursive call to take 2, another
            to skip 3, and another to take 4.

            Using this approach, we need a recursive call to take 2 and from 2,
            we can directly loop to 4 instead of having to need an extra recursive
            call to skip 3.

    Runtime:
        We removed the redundant recursive calls, but we are still simulating a
        binary choice of choosing or skipping each number. Thus, the time complexity
        is the same as Solution2, O(2^(t/m)).

    Memory:
        The call stack takes O(h) where h is the height of the recursion tree.
        In the worst case, we can have a combination of length t/m. Therefore,
        the overall memory complexity is O(t/m).
    """

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(startIx, currNums, currSum):
            if currSum == target:
                res.append(currNums.copy())
                return

            for k in range(startIx, len(nums)):
                if currSum + nums[k] > target:
                    return

                currNums.append(nums[k])
                dfs(k, currNums, currSum + nums[k])
                currNums.pop()

        dfs(0, [], 0)
        return res
