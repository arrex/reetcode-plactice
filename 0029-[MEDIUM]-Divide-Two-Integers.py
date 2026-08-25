class Solution:
    """
    Intuition:
        Our solution builds off the concept that any integer quotient
        can be expressed as a linear combination of powers of 2.

        The problem asking us to round down in our division is the
        same as asking us to implement integer division.

        The idea is to bit shift the divisor until we cannot fit it
        in our dividend anymore. Then, we simple note the multiple
        for that iteration and increment our quotient.

    Runtime:
        The outer while loop has log n iterations as it shrinks the
        dividend by a power of 2 at least every turn.

        The inner while loop also runs in log n iterations as it can
        shift the divisor up to log n times at most.

        Thus, the overall runtime is O((log n)^2).

    Memory:
        O(1).
    """

    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1

        isNeg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            currDivisor = divisor
            multiple = 1

            while dividend >= (currDivisor << 1):
                currDivisor <<= 1
                multiple <<= 1

            dividend -= currDivisor
            quotient += multiple

        res = -quotient if isNeg else quotient

        res = max(res, MIN)
        res = min(res, MAX)

        return res
