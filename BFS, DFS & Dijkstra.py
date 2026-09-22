from collections import deque
import heapq

# Create graph
g = [[] for _ in range(6)]


def add(u, v, w):
    g[u].append((v, w))
    g[v].append((u, w))


# Add edges
for e in (
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5),
    (3, 4, 3)
):
    add(*e)


# BFS
def bfs(s):
    seen = {s}
    q = deque([s])
    out = []

    while q:
        u = q.popleft()
        out.append(u)

        for v, _ in g[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)

    return out


# DFS
def dfs(s):
    seen = set()
    out = []

    def visit(u):
        seen.add(u)
        out.append(u)

        for v, _ in g[u]:
            if v not in seen:
                visit(v)

    visit(s)
    return out


# Dijkstra
def dijkstra(s):
    d = [float('inf')] * len(g)
    d[s] = 0

    pq = [(0, s)]

    while pq:
        du, u = heapq.heappop(pq)

        if du != d[u]:
            continue

        for v, w in g[u]:
            nd = du + w

            if nd < d[v]:
                d[v] = nd
                heapq.heappush(pq, (nd, v))

    return d


print("BFS:", *bfs(0))
print("DFS:", *dfs(0))

distances = dijkstra(0)

print(
    "Distance:",
    *(
        "INF" if x == float('inf') else x
        for x in distances
    )
)