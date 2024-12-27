# Advent of Code 2024: Day 16
from aoc import get_data, printd, set_debug, get_debug
from collections import defaultdict
import heapq
from tqdm import tqdm

set_debug(False)
data = get_data(16, splitlines=True, year_num=2024)

printd("Input data:")
for line in data:
    printd(line)

# moving one step ahead "costs" 1, turning 90 degrees "costs" 1000
weights = {
    "move": 1,
    "turn": 1000,
}

# Find start and end positions
start = None
end = None
for y, row in enumerate(data):
    for x, char in enumerate(row):
        if char == "S":
            start = (x, y)
        if char == "E":
            end = (x, y)

print(f"\nStart position: {start}")
print(f"End position: {end}")

def get_neighbors(pos, direction, maze):
    """Get valid neighboring positions and their costs"""
    x, y = pos
    dx, dy = direction
    neighbors = []
    
    # All possible directions: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for new_dx, new_dy in directions:
        new_x = x + new_dx
        new_y = y + new_dy
        
        # Check if the new position is within bounds and not a wall
        if (0 <= new_x < len(maze[0]) and 
            0 <= new_y < len(maze) and 
            maze[new_y][new_x] != '#'):
            
            # Calculate cost - if direction changes, add turning cost
            cost = weights["move"]
            if (new_dx, new_dy) != direction:
                cost += weights["turn"]
            
            neighbors.append(((new_x, new_y), (new_dx, new_dy), cost))
    
    return neighbors

def find_paths(maze, start, end):
    """Find all paths with the lowest cost from start to end"""
    if not start or not end:
        print("Error: Start or end position not found!")
        return float('inf'), [], set()
        
    # Priority queue for Dijkstra's algorithm
    # Format: (total_cost, position, direction, path)
    initial_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Try all initial directions
    queue = [(0, start, d, [start]) for d in initial_directions]
    heapq.heapify(queue)
    
    # Keep track of visited states and their costs
    visited = {}  # (position, direction) -> (cost, path)
    
    # Track the lowest cost to end and all paths with that cost
    lowest_cost = float('inf')
    lowest_cost_paths = []
    
    steps = 0
    while queue:
        cost, pos, direction, path = heapq.heappop(queue)
        steps += 1
        
        if steps % 1000 == 0:
            printd(f"Step {steps}, Current position: {pos}, Cost: {cost}")
        
        # If cost is already higher than the lowest cost found, skip
        if cost > lowest_cost:
            continue
            
        # If we reached the end
        if pos == end:
            if cost < lowest_cost:
                # Found a new lowest cost path
                lowest_cost = cost
                lowest_cost_paths = [path]
            elif cost == lowest_cost:
                # Found another path with the same lowest cost
                lowest_cost_paths.append(path)
            continue
        
        # Skip if we've seen this state with a lower cost
        state = (pos, direction)
        if state in visited and visited[state][0] <= cost:
            continue
        
        visited[state] = (cost, path)
        
        # Check all neighbors
        for new_pos, new_dir, move_cost in get_neighbors(pos, direction, maze):
            new_cost = cost + move_cost
            
            # Only continue if this path could potentially be a lowest cost path
            if new_cost <= lowest_cost:
                new_path = path + [new_pos]
                new_state = (new_pos, new_dir)
                
                if new_state not in visited or new_cost < visited[new_state][0]:
                    heapq.heappush(queue, (new_cost, new_pos, new_dir, new_path))

    # Get unique cells from all lowest cost paths
    unique_cells = set()
    printd(f"Found {len(lowest_cost_paths)} paths with lowest cost {lowest_cost}")
    for path in lowest_cost_paths:
        unique_cells.update(path)
    
    return lowest_cost, lowest_cost_paths, unique_cells


lowest_cost, paths, unique_cells = find_paths(data, start, end)

for x,y in tqdm(paths[0]):
    maze_new = data.copy()
    # Replace the path with a "#"
    maze_new[y] = maze_new[y][:x] + "#" + maze_new[y][x+1:]
    new_lowest_cost, new_paths, new_unique_cells = find_paths(maze_new, start, end)
    if new_lowest_cost == lowest_cost:
        # add the unique cells to the set
        unique_cells.update(new_unique_cells)

print("\n")
print(f"Lowest cost: {lowest_cost}")
print(f"Unique cells in all paths with lowest cost: {len(unique_cells)}")