class Solution1:
    """
    Intuition:
        Brute force approach. Linear scan over all numbers in the interval
        and check individual digits.

    Runtime:
        O(n * k) where n is the input and k is the number of digits of the
        greatest number within range. Constraint specifies upper bound of
        n to be 10^4, so 5 digits at most -> O(5n).

    Memory:
        O(1).
    """

    def rotatedDigits(self, n: int) -> int:
        res = 0
        rotateMap = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        for i in range(1, n + 1):
            num = i
            rotatedNum = 0
            exp = 0

            while num:
                digit = num % 10
                if digit in [3, 4, 7]:
                    break  # exit early
                num = num // 10

                rotatedDigit = rotateMap[digit]
                rotatedNum += rotatedDigit * (10**exp)
                exp += 1

            # only incr if num fully rotated
            # and input != rotated output
            if not num and i != rotatedNum:
                res += 1

        return res


class Solution2:
    """
    Intuition:
        Use digit DP approach. Top-down since we recurse from pos=0 and memoize
        on the way back up.

        Our memo table has 3 dimensions for the 3 "pieces" of state we need to
        carry forward to solve the next step: the current digit's position, if
        the bound is tight or not (constrains the next digit we can select...
        if tight, then bound to input prefix, else can choose whatever digit),
        and if the rotated version incurs a change (e.g. 1 rotated does not
        change, we track if the prefix has incurred a change so far).

        We initialize the memo table with sentinel values to disinguish between
        computed and uncomputed steps.

        The base case in our recursive DP helper function checks if we have
        selected all digits and if the rotated digit incurs a change. We also
        peek the memo table and return the value of our current state if it is
        stored.

        Then, we compute what our next digit's limit is and iterate through
        the candidates. We prune invalid candidates (do not yield valid rotations),
        recursively compute subproblems, and populate the memo table.

    Runtime:
        Let D be the number of digits we have to pick (bound by 5 via constraints
        with n = 10^4). 'tight' can take 2 possible values (0/1 for F/T respectively)
        and 'has_change' as well. This gives us 2 * 2 * D = 4 * D possible states.

        At each step, we can choose 10 possible digits which represents the amount of
        work we have to do.

        Thus, the runtime complexity is O(10 * (4 * D)) ~ O(40 * D) ~ O(D) ~ O(1) since
        D <= 5.

    Memory:
        O(4 * D) ~ O(D) since we need to memoize potentially all states. Here, D is the
        number of digits in the input 'n'.
    """

    def rotatedDigits(self, n: int) -> int:
        # position, tight, has_change -> -1 = uninitialized state
        memo = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(5)]
        digits = str(n)

        def dp(pos, tight, has_change):
            # base case -- we have finished constructing our number
            if pos == len(digits):
                return 1 if has_change else 0

            if memo[pos][tight][has_change] != -1:
                return memo[pos][tight][has_change]

            limit = int(digits[pos]) if tight else 9
            res = 0
            for d in range(limit + 1):
                # prune branches of invalid digits
                if d in [3, 4, 7]:
                    continue

                # recurse to next step with updated state
                # - pos advances by 1
                # - tight = 1 only if previously tight AND curr
                #   digit matches digits prefix at curr pos
                # - has_change = 1 if curr digit rotates to smth
                #   diff or previous digits incur change
                res += dp(
                    pos + 1,
                    1 if tight and d == int(digits[pos]) else 0,
                    1 if (d in [2, 5, 6, 9]) or has_change else 0,
                )

            memo[pos][tight][has_change] = res
            return res

        # start with initial tight state = 1 to constrain to n
        return dp(0, 1, 0)
