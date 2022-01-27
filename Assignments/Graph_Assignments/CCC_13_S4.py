import sys

input = sys.stdin.readline

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]


def bfs(x, y):
    visited = [False] * (N + 1)
    q = [x]
    visited[x] = True
    while q:
        u = q.pop(0)
        for v in adj[u]:
            if v == y:
                return True
            if not visited[v]:
                q.append(v)
                visited[v] = True
    return False


for _ in range(M):
    raw_input = input().split()
    x, y = int(raw_input[0]), int(raw_input[1])
    adj[x].append(y)

raw_input = input().split()
p, q = int(raw_input[0]), int(raw_input[1])

if bfs(p, q):
    print("yes")
elif bfs(q, p):
    print("no")
else:
    print("unknown")