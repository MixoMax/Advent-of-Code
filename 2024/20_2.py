# Advent of Code 2024: Day 20
# @Author: Linus Horn
from aoc import get_data, printd, set_debug, get_debug, nums
from collections import defaultdict
import heapq

set_debug(True)
data: list[str] = get_data(day_num=20, splitlines=True)

grid = tuple(data)
rows = len(grid)
cols = len(grid[0])

# Find start and end positions
start = None
end = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def dijkstra(start: tuple[int, int], end: tuple[int, int] = None) -> dict[tuple[int, int], int]:
    """Returns distances from start to all reachable positions"""
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    q = [(0, start)]
    visited = set()
    
    while q:
        dist, (r, c) = heapq.heappop(q)
        if (r, c) == end:
            break
            
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                new_dist = dist + 1
                if new_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_dist
                    heapq.heappush(q, (new_dist, (nr, nc)))
    
    return distances

# Calculate distances from end to all positions
distances_to_end = dijkstra(end)
# Calculate distances from start to all positions
distances_from_start = dijkstra(start)

def find_cheats():
    cheats = set()
    MAX_CHEAT_DISTANCE = 20
    
    # For each potential cheat starting position
    for sr in range(rows):
        for sc in range(cols):
            start_pos = (sr, sc)
            if grid[sr][sc] == '#' or distances_from_start[start_pos] == float('inf'):
                continue
                
            # For each potential cheat ending position within Manhattan distance of 20
            for er in range(max(0, sr - MAX_CHEAT_DISTANCE), min(rows, sr + MAX_CHEAT_DISTANCE + 1)):
                for ec in range(max(0, sc - MAX_CHEAT_DISTANCE), min(cols, sc + MAX_CHEAT_DISTANCE + 1)):
                    end_pos = (er, ec)
                    if grid[er][ec] == '#' or distances_to_end[end_pos] == float('inf'):
                        continue
                        
                    # Check if within cheat range
                    cheat_distance = manhattan_distance(start_pos, end_pos)
                    if cheat_distance > MAX_CHEAT_DISTANCE:
                        continue
                    
                    # Calculate total path length with cheat
                    total_distance = (
                        distances_from_start[start_pos] +  # Distance to cheat start
                        cheat_distance +                   # Cheat length
                        distances_to_end[end_pos]          # Distance from cheat end to maze end
                    )
                    
                    # Calculate time saved
                    normal_distance = distances_to_end[start]  # Distance without any cheats
                    time_saved = normal_distance - total_distance
                    
                    if time_saved > 0:
                        cheats.add((time_saved, start_pos, end_pos))
    
    return cheats

cheats = find_cheats()
print(f"Found {len(cheats)} cheats")

max_time_saved = max(cheats, key=lambda x: x[0])[0]
print(f"Maximum time saved: {max_time_saved}")

cutoff = 100
n_cheats_with_cutoff = sum(1 for cheat in cheats if cheat[0] >= cutoff)
print(f"Number of cheats with time saved >= {cutoff}: {n_cheats_with_cutoff}")