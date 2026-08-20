from collections import defaultdict


class Solution:
    """
    Intuition:
        Notice that the maximum amount of groups we can seat in a row is 2
        when there are no reservations.

        Notice also that seats 1 and 10 are irrelevant since they do not
        belong to any valid section we can seat groups in.

        Notice lastly that if a row has even one seat reserved between seats
        2 and 9 inclusively, then the maximum amount of groups we can seat
        is 1.

        With these observations, we can model each row as a bit mask where
        1-bits are reserved seats and 0 are unreserved.

        We can then take this bit mask and decode it to a value to determine
        how many groups we can seat in the row.

        Finally, for rows without any reservations, we can greedily assign 2
        groups.

    Runtime:
        O(k) to process each elmt in `reservedSeats`.

        O(n) to process each row and decode to number of groups we can seat.

        Overall, O(n + k) runtime.

    Memory:
        O(1) for the `ENCODE` array.

        O(1) for the `DECODE` array.

        O(n) for the `rows` dictionary.

        Overall, O(n) memory.
    """

    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        # this array helps us build the bit mask, each seat is assigned to a
        # power of 2.
        #
        # seats are 1-indexed, so index 0 contains 0 to not alter the bit mask.
        #
        # seats 1 and 10 are also irrelevant since we cannot seat people in
        # this sections, so they also encode to 0.
        ENCODE = [0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 0]
        # this array helps us decode a bit mask to the number of groupings we can
        # assign.
        #
        # 15 =  00001111
        # 60 =  00111100
        # 240 = 11110000
        #
        # note that if there is ONE reservation within seats 2-9 inclusive, the
        # most amt of groups we can assign is 1
        DECODE = [2] + [int(not (i & 240) or not (i & 60) or not (i & 15)) for i in range(1, 256)]
        rows = defaultdict(int)

        for row, seat in reservedSeats:
            rows[row] |= ENCODE[seat]

        # decode for each row using DECODE arr
        # for rows without any reservations, we can seat 2 groups by default
        return sum(DECODE[row] for row in rows.values()) + 2 * (n - len(rows))
