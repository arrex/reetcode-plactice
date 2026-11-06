from typing import List


class Solution:
    """
    Intuition:
        We can sort the logs and queries by time so that we can process
        them efficiently. At any point, we look at a given window of
        and store the frequency of their requests to see which ones have
        none. Then, we simply slide the window to the next query's time
        range. The sliding window approach avoids duplicate work when
        two subsequent time range queries have overlap.

    Runtime:
        Suppose we have n servers, l logs, and q queries.

        Sorting the logs takes O(l log l).

        Storing the indices of the queries takes O(q).

        Sorting the queries takes O(q log q).

        Our sliding window loop needs to process O(q) queries. Each log is
        processed at most twice, meaning O(l). So the loop takes O(q + l)
        time.

        Thus, our overall runtime is O(l log l + q + q log q + q + l) which
        simplifies to O(l log l + q log q) runtime.

    Memory:
        Sorting the logs takes up at worst O(l) space. O(q) for sorting queries.

        Tracking the query indices in a hashmap takes O(q) space.

        The frequency counter window array takes O(n) space.

        Overall, the total auxiliary memory complexity is O(l + q + n).
    """

    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sort logs by time
        logs.sort(key=lambda x: x[1])

        # keep track of original ordering of queries
        qmap = {q: ix for ix, q in enumerate(queries)}

        # sort queries by time
        queries.sort()

        # sliding window
        res = [0] * len(queries)
        window = [0] * n
        active = 0
        l, r = 0, 0
        for q in queries:
            # expand right ptr
            while r < len(logs) and logs[r][1] <= q:
                sid, _ = logs[r]

                window[sid - 1] += 1
                if window[sid - 1] == 1:
                    active += 1

                r += 1

            # adjust left ptr
            while l < r and logs[l][1] < q - x:
                sid, _ = logs[l]

                window[sid - 1] -= 1
                if window[sid - 1] == 0:
                    active -= 1

                l += 1

            res[qmap[q]] = n - active

        return res
