import heapq
from collections import Counter, deque
from typing import List


class Solution1:
    """
    Intuition:
        Intuitively, we know that we have to start by processing
        the most frequent task. We resort to a maxHeap for efficient
        retrieval based on highest frequency.

        Then, we need a data structure to model the cooldown period.
        For this, we use a queue where each element contains the
        remaining frequency of the current task as well as the time
        value at which it can be scheduled again (after the cooldown).

    Runtime:
        Computing the frequency of the tasks takes O(n).

        For building the heap, we have a runtime of O(K log K) where
        K is the number of tasks. We know that there are at most 26
        unique tasks (number of letters in alphabet), so the runtime
        simplifies to O(1).

        The while loop either idles or decrements the frequency of a
        task. Given that we have n tasks, the runtime resolves to O(n)
        since each task needs to be treated.

        Overall, we have a runtime of O(n).

    Memory:
        O(1) for the heap and queue since there are at most 26 letters.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        maxHeap = []
        for v in freq.values():
            heapq.heappush(maxHeap, -v)

        # cooldown queue: store as (freq, cooldown end time)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                # +1 since we are dealing with negative values
                # equivalent of decrementing by 1...
                f = heapq.heappop(maxHeap) + 1

                if f < 0:
                    q.append((f, time + n))

            if q and q[0][1] == time:
                f, _ = q.popleft()
                heapq.heappush(maxHeap, f)

        return time


class Solution2:
    """
    Intuition:
        The task with the highest freq determines the minimum possible
        schedule length because it will need the most idle time to
        satisfy the cooldown constraint.

        Considering this, we can create 'cycles' of processing the most
        frequent task and then waiting (can be processing other tasks or
        simply idling) for n clock cycles. This gives us a cycle length
        of n + 1 (waiting + processing the most frequent task itself).

        We have the max frequency and a cycle length of n + 1, so we can
        multiply these two to get the minimum amount of time needed. Note
        that the last occurrence of the most frequent task does not need
        trailing slots, so the factor is only (maxFreq - 1).

        If there are multiple tasks with frequence maxFreq, then they all
        need to be placed in these intervals. They also will need to be
        appended on the last occurrence which explains the addition.

        Lastly, consider the case where the cooldown is 1 and each task
        has the same frequence of 1000. Since you can't finish faster than
        the number of tasks, we need to return the max between the time
        we obtained from our calculations and the number of tasks at hand.

    Runtime:
        O(n) to compute counts and find maxFreq.

        O(26) to find other tasks with frequency = maxFreq which
        simplifies to O(1).

        Overall O(n) runtime.

    Memory:
        O(1) since we have at most 26 letters.
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxFreq = max(c.values())

        # by processing most frequent task first
        time = (maxFreq - 1) * (n + 1)

        # accounting for other tasks with frequency = maxFreq as well
        cnt = 0
        for f in c.values():
            if f == maxFreq:
                cnt += 1

        time += cnt
        return max(time, len(tasks))
