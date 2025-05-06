class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = {}
        paths=defaultdict(list)
        for source,dest,cost in flights:
            paths[source].append(dest)
            costs[(source,dest)] = cost
        dp=[float("inf")]*n
        minCost = float("inf")
        currQ = [(src,-1,0)]

        while currQ:
            currStop,noStops,cost = currQ.pop(0)

            if noStops > k:
                continue
            
            if dp[currStop] <= cost:
                continue
            else:
                dp[currStop] = cost

            if currStop == dst:
                continue
            
            for dests in paths[currStop]:
                currQ.append((dests,noStops+1,cost+costs[(currStop,dests)]))

        return -1 if dp[dst] == float("inf") else dp[dst]


