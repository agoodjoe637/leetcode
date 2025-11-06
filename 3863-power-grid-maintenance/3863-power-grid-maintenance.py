from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def processQueries(
        self, c: int, connections: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        online = set()
        station_group_ids = {}
        min_heaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            station_group_ids[station] = group_id
            heappush(min_heaps[group_id], station)

            for neighbor in adj[station]:
                dfs(neighbor, group_id)

        id = 0
        for station in range(1, c + 1):
            dfs(station, station)
        answer = []
        for query_type, query_station in queries:
            if query_type == 1:
                if query_station in online:
                    answer.append(query_station)
                    continue
                group_id = station_group_ids[query_station]
                min_heap = min_heaps[group_id]
                while min_heap and min_heap[0] not in online:
                    heappop(min_heap)
                if min_heap:
                    answer.append(min_heap[0])
                else:
                    answer.append(-1)
            else:
                online.discard(query_station)

        return answer
