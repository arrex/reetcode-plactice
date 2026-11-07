import heapq
from collections import deque


class Solution:
    """
    Intuition:
        Use a min-heap for available servers keyed on the weight of the server (and index to tie-break).
        Use a min-heap for busy servers keyed on the deadline (i.e. when server will become available)
        again. Use a job queue to process jobs in chronological order.

        The idea is that if we can assign a job to an idle server directly, we will do so. Otherwise, we
        append it to the job queue and wait for the next server to become free to assign it.

    Runtime:
        Suppose n denotes the number of servers and m denotes the number of tasks.

        O(n) to build a heap of idle servers.

        The first for-loop has m iterations. We have while-loops, but notice how each task is assigned
        once and each server transition is associated with a task. Thus, the while-loops are on the
        scale of O(m). However, each task assignment requires us to push/pop from the server heaps,
        leadging to O(log n) for each of the O(m) calls. Thus, we have O(m + m log n) ~ O(m log n).

        We apply the same idea to the second while-loop, which gives us O(m log n) for it too.

        Overall, we have O(n + m log n) runtime.

    Memory:
        O(n) for idle and busy server heaps.

        O(m) for the job queue.

        Overall, O(n + m) auxiliary space.
    """

    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # init idle server pool
        idle = [(s, ix) for ix, s in enumerate(servers)]
        heapq.heapify(idle)

        # init busy server pool -> holds (deadline, (server, ix))
        busy = []

        # init job queue
        q = deque()

        res = []
        for time, duration in enumerate(tasks):
            # move busy servers who are done to idle
            while busy and time >= busy[0][0]:
                _, worker = heapq.heappop(busy)
                heapq.heappush(idle, worker)

            # process from job queue
            while idle and q:
                worker = heapq.heappop(idle)
                dur = q.popleft()
                heapq.heappush(busy, (time + dur, worker))
                res.append(worker[1])

            # curr task can be processed directly
            if idle:
                worker = heapq.heappop(idle)
                heapq.heappush(busy, (time + duration, worker))
                res.append(worker[1])
            else:  # curr task needs to be enqueued
                q.append(duration)

        if not q:
            return res

        while q:
            duration = q.popleft()

            # update time only if we don't have any idle servers
            if not idle:
                time = busy[0][0]

            # remove all completed
            while busy and time >= busy[0][0]:
                _, worker = heapq.heappop(busy)
                heapq.heappush(idle, worker)

            # execute next task
            worker = heapq.heappop(idle)
            heapq.heappush(busy, (time + duration, worker))
            res.append(worker[1])

        return res
