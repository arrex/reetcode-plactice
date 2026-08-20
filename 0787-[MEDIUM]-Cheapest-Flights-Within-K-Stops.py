import heapq
from math import inf


class Solution1:
    """
    Intuition:
        Using Bellman-Ford algorithm. At each iteration of the
        for loop, we are propagating min costs across an extra
        stop from each node. At the end, we can just peek the
        price at the index of our destination airport.

    Runtime:
        Suppose we have n flights available.

        The outer for loop takes k iterations. For each of those
        k iterations, we need to create a new array to hold the
        updated prices and iterate through all flights which both
        take O(N) time.

        Thus, the total runtime is O(k * n).

    Memory:
        The prices array takes O(n) space.

        Every tmp array we allocate also takes O(n) space.

        Overall, O(n) memory complexity.
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]
            for u, v, cost in flights:
                tmp[v] = min(tmp[v], prices[u] + cost)
            prices = tmp  # update layer

        return prices[dst] if prices[dst] < inf else -1


class Solution2:
    """
    Intuition:
        Use Dijkstra's algorithm. We greedily explore paths based
        on total price in the hopes of reaching the destination as
        soon as possible.

        We prune paths by checking if we can afford to make stops
        still or by checking if there is a lower price path to
        the given node WITH THE SAME NUMBER OF STOPS. It is impo-
        rtant to note that a lesser cost at a given point does not
        equate to a lesser cost down the line! A more expensive
        flight path for the current node might yield a cheaper path
        to the final destination.

    Runtime:
        Suppose we have V cities and E flights.

        Building the adj list takes O(E).

        We have V cities and k stops meaning V * k possible states.
        Pushing/popping a state into/from the prio queue takes at
        most O(log(V * k)) time, but we only do this work when we relax
        an edge. We have E edges and each is relaxed up to k times,
        yielding an overall runtime of O(E * k * log(V * k)).

        Overall runtime is O(E * k * log(V * k)).

    Memory:
        Adj list takes O(E) space.

        The best dict stores up to V * k elements, leading to O(V * k)
        space.

        The priority queue holds at most all states of which we have
        V * k i.e. O(V * k) memory.

        Overall, we have O(E + V * k) memory.
    """

    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append((v, cost))

        best = {}
        pq = [(0, src, 0)]
        while pq:
            price, curr, stops = heapq.heappop(pq)

            if curr == dst:
                return price

            if stops <= k:
                for nei, cost in adj[curr]:
                    new_price = price + cost
                    state = (nei, stops + 1)

                    if state not in best or new_price < best[state]:
                        best[state] = new_price
                        heapq.heappush(pq, (new_price, nei, stops + 1))

        return -1
