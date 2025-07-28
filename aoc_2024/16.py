# Advent of Code 2024: Day 16
from aoc import get_data, printd, set_debug, get_debug
from collections import defaultdict
import heapq

set_debug(True)
data = get_data(16, splitlines=True, year_num=2024)

print("Input data:")
for line in data:
    print(line)

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

def find_path(maze, start, end):
    """Find the lowest cost path from start to end"""
    if not start or not end:
        print("Error: Start or end position not found!")
        return float('inf')
        
    # Priority queue for Dijkstra's algorithm
    # Format: (total_cost, position, direction)
    initial_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Try all initial directions
    queue = [(0, start, d) for d in initial_directions]
    heapq.heapify(queue)
    
    # Keep track of visited states and their costs
    visited = {}  # (position, direction) -> cost
    
    steps = 0
    while queue:
        cost, pos, direction = heapq.heappop(queue)
        steps += 1
        
        if steps % 1000 == 0:
            print(f"Step {steps}, Current position: {pos}, Cost: {cost}")
        
        # If we reached the end, return the cost
        if pos == end:
            return cost
        
        # Skip if we've seen this state with a lower cost
        state = (pos, direction)
        if state in visited and visited[state] <= cost:
            continue
        
        visited[state] = cost
        
        # Check all neighbors
        for new_pos, new_dir, move_cost in get_neighbors(pos, direction, maze):
            new_cost = cost + move_cost
            new_state = (new_pos, new_dir)
            
            if new_state not in visited or new_cost < visited[new_state]:
                heapq.heappush(queue, (new_cost, new_pos, new_dir))

    print("No path found!")
    return float('inf')


lowest_cost = find_path(data, start, end)
print(f"\nLowest cost path: {lowest_cost}")
