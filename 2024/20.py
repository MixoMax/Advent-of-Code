# Advent of Code 2024: Day 20
# @Author: Linus Horn
from aoc import get_data, printd, set_debug, get_debug, nums
from tqdm import tqdm
from functools import cache
import heapq

set_debug(True)
data: list[str] = get_data(day_num=20, splitlines=True)

grid = tuple(data)
rows = len(grid)
cols = len(grid[0])

start = None
end = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

@cache
def dijkstra(grid: tuple[str], start: tuple[int, int], end: tuple[int, int], allow_cheat: bool = False) -> int:
    q = [(0, start)]
    visited = set()
    while q:
        dist, (r, c) = heapq.heappop(q)
        if (r, c) == end:
            return dist
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' or allow_cheat:
                    heapq.heappush(q, (dist + 1, (nr, nc)))
    return float('inf')

shortest_path_time = dijkstra(grid, start, end)

def find_cheats():
    cheats = set()  # Store unique cheats by (start_pos, end_pos)
    
    # For each possible starting position of a cheat
    for sr in tqdm(range(rows)):
        for sc in range(cols):
            if grid[sr][sc] != '#':  # Must start from valid position
                # Get time to reach cheat start
                time_to_start = dijkstra(grid, start, (sr, sc))
                if time_to_start == float('inf'):
                    continue
                    
                # Try all possible 2-move sequences through walls
                for dr1, dc1 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    pos1 = (sr + dr1, sc + dc1)
                    if not (0 <= pos1[0] < rows and 0 <= pos1[1] < cols):
                        continue
                        
                    for dr2, dc2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        end_r = pos1[0] + dr2
                        end_c = pos1[1] + dc2
                        if not (0 <= end_r < rows and 0 <= end_c < cols):
                            continue
                            
                        # End position must be valid track
                        if grid[end_r][end_c] == '#':
                            continue
                            
                        # Calculate total time with this cheat
                        time_to_end = dijkstra(grid, (end_r, end_c), end)
                        if time_to_end == float('inf'):
                            continue
                            
                        total_time = time_to_start + 2 + time_to_end  # 2 moves during cheat
                        time_saved = shortest_path_time - total_time
                        
                        if time_saved > 0:
                            cheats.add((time_saved, (sr, sc), (end_r, end_c)))
                            
    return cheats

cheats = find_cheats()
cuttoff = 100
print(f"Found {len(cheats)} cheats")

n_cheats_with_cutoff = 0
for time_saved, _, _ in sorted(cheats, reverse=True):
    if time_saved >= cuttoff:
        n_cheats_with_cutoff += 1
    else:
        break

print(f"Number of cheats that save at least {cuttoff} picoseconds: {n_cheats_with_cutoff}")

