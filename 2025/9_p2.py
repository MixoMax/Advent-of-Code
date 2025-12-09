from aoc import get_data
from bisect import bisect_right

data_lines, _ = get_data(day_num=9, year_num=2025)

corner_candidates = []
for line in data_lines:
    x,y = map(int, line.split(","))
    corner_candidates.append((x,y))

N = len(corner_candidates)

# Build polygon edges
# Vertical edges: (x, y_min, y_max)
# Horizontal edges: (y, x_min, x_max)
edges_v = []
edges_h = []

for i in range(N):
    p1 = corner_candidates[i]
    p2 = corner_candidates[(i + 1) % N] # Wrap around

    if p1[0] == p2[0]:
        edges_v.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
    else:
        edges_h.append((p1[1], min(p1[0], p2[0]), max(p1[0], p2[0])))

# Sort points by X for "vertex strictly inside" check
points_by_x = sorted(corner_candidates, key=lambda p: p[0])

# Sort edges for edge crossing and ray casting checks
edges_v.sort(key=lambda e: e[0])
edges_h.sort(key=lambda e: e[0])

def is_inside(x, y):
    # is point on a vertical boundary?
    idx = bisect_right(edges_v, (x, float('inf'), float('inf')))
    i = idx - 1
    while i >= 0 and edges_v[i][0] == x:
        if edges_v[i][1] <= y <= edges_v[i][2]:
            return True
        i -= 1
        
    # is point on a horizontal boundary?
    idx = bisect_right(edges_h, (y, float('inf'), float('inf')))
    i = idx - 1
    while i >= 0 and edges_h[i][0] == y:
        if edges_h[i][1] <= x <= edges_h[i][2]:
            return True
        i -= 1
        
    # cast ray to the right
    # Count intersections with vertical edges where edge_x > x
    intersections = 0
    start_idx = bisect_right(edges_v, (x, float('inf'), float('inf')))
    
    for k in range(start_idx, len(edges_v)):
        ex, ey1, ey2 = edges_v[k]
        # include lower bound, exclude upper bound to correctly handle rays passing exactly through vertices
        if ey1 <= y < ey2:
            intersections += 1
            
    return (intersections % 2) == 1

max_area = 0

for i in range(N):
    p1 = corner_candidates[i]
    for j in range(i + 1, N):
        p2 = corner_candidates[j]
        
        w = abs(p1[0] - p2[0]) + 1
        h = abs(p1[1] - p2[1]) + 1
        area = w * h
        
        if area <= max_area:
            continue
        
        xmin, xmax = min(p1[0], p2[0]), max(p1[0], p2[0])
        ymin, ymax = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        valid_rect = True
        

        # check if the rectangle contains a hole, making it invalid
        start_x_idx = bisect_right(points_by_x, (xmin, float('inf')))
        for k in range(start_x_idx, N):
            px, py = points_by_x[k]
            if px >= xmax:
                break
            if ymin < py < ymax:
                valid_rect = False
                break
        if not valid_rect:
            continue
            
        # Vertical edges crossing the width? (ex in (xmin, xmax) and covering height)
        idx_v = bisect_right(edges_v, (xmin, float('inf'), float('inf')))
        for k in range(idx_v, len(edges_v)):
            ex, ey1, ey2 = edges_v[k]
            if ex >= xmax:
                break
            if ey1 <= ymin and ey2 >= ymax:
                valid_rect = False
                break
        if not valid_rect:
            continue

        # Horizontal edges crossing the height? (ey in (ymin, ymax) and covering width)
        idx_h = bisect_right(edges_h, (ymin, float('inf'), float('inf')))
        for k in range(idx_h, len(edges_h)):
            ey, ex1, ex2 = edges_h[k]
            if ey >= ymax:
                break
            if ex1 <= xmin and ex2 >= xmax:
                valid_rect = False
                break
        if not valid_rect:
            continue
            
        # The original corners p1, p2 are vertices, so they are definitely inside/boundary.
        # We must check (p1.x, p2.y) and (p2.x, p1.y).
        if not is_inside(p1[0], p2[1]): continue
        if not is_inside(p2[0], p1[1]): continue
        
        # If all checks pass, we found a valid rectangle
        # since we checked area > max_area earlier, we can update directly
        max_area = area

print(max_area)
