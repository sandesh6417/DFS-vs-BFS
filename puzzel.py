import time
from collections import deque

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def neighbors(state):
    idx = state.index(0)
    r, c = divmod(idx, 3)
    moves = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr * 3 + nc
            new_state = list(state)
            new_state[idx], new_state[nidx] = new_state[nidx], new_state[idx]
            moves.append(tuple(new_state))

    return moves


def bfs(start):
    frontier = deque([start])
    visited = {start}
    nodes_expanded = 0
    parent = {start: None}

    if start == GOAL:
        return [], 0

    while frontier:
        state = frontier.popleft()
        nodes_expanded += 1

        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = state

                if nxt == GOAL:
                    # Reconstruct path
                    path = []
                    s = nxt

                    while s is not None:
                        path.append(s)
                        s = parent[s]

                    return path[::-1], nodes_expanded

                frontier.append(nxt)

    return None, nodes_expanded


def dfs(start, max_depth=30):
    # Iterative DFS with explicit stack,
    # visited set, and depth limit to avoid explosion
    stack = [(start, 0)]
    visited = {start}
    nodes_expanded = 0
    parent = {start: None}

    if start == GOAL:
        return [], 0

    while stack:
        state, depth = stack.pop()
        nodes_expanded += 1

        if depth >= max_depth:
            continue

        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = state

                if nxt == GOAL:
                    path = []
                    s = nxt

                    while s is not None:
                        path.append(s)
                        s = parent[s]

                    return path[::-1], nodes_expanded

                stack.append((nxt, depth + 1))

    return None, nodes_expanded


# A solvable, moderately shuffled start
# (not too easy, not unsolved by DFS depth limit)
START = (1, 2, 3, 4, 0, 6, 7, 5, 8)


def run_trials(fn, runs=3):
    times = []
    nodes = None
    path_len = None

    for _ in range(runs):
        t0 = time.perf_counter()
        path, nodes_expanded = fn(START)
        t1 = time.perf_counter()

        times.append((t1 - t0) * 1000)  # ms
        nodes = nodes_expanded
        path_len = (len(path) - 1) if path else None

    avg_time = sum(times) / len(times)
    return avg_time, nodes, path_len, times


if __name__ == "__main__":
    print("Start state:", START)
    print()

    bfs_time, bfs_nodes, bfs_pathlen, bfs_times = run_trials(bfs, runs=3)

    print(
        f"BFS: avg_time={bfs_time:.4f} ms, "
        f"nodes_expanded={bfs_nodes}, "
        f"path_length={bfs_pathlen}, runs={bfs_times}"
    )

    dfs_time, dfs_nodes, dfs_pathlen, dfs_times = run_trials(dfs, runs=3)

    print(
        f"DFS: avg_time={dfs_time:.4f} ms, "
        f"nodes_expanded={dfs_nodes}, "
        f"path_length={dfs_pathlen}, runs={dfs_times}"
    )
