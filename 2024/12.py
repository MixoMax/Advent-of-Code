# Advent of Code 2024: Day 12
from aoc import get_data
from dataclasses import dataclass
from tqdm import tqdm
data = get_data(12, splitlines=True)

plants = {} # {char: [(x, y)]} where x, y are coordinates of plant
print("  ", " ".join(str(i) for i in range(len(data[0]))), end=" ")
for y, row in enumerate(data):
    print("\n", y, end=" ")
    for x, char in enumerate(row):
        print(char, end=" ")
        if plants.get(char):
            plants[char].append((x, y))
        else:
            plants[char] = [(x, y)]
    
print()

#print(plants)

@dataclass
class PlantRegion:
    # a contiguous region of plants of the same type (char)
    char: str
    size: int
    outer_coords: list[tuple[int, int]]
    coords: list[tuple[int, int]]

    def _perimeter(self):
        # return the perimeter of the region
        perimter = 0
        for x, y in self.outer_coords:
            if (x, y+1) not in self.outer_coords:
                perimter += 1
            if (x, y-1) not in self.outer_coords:
                perimter += 1
            if (x+1, y) not in self.outer_coords:
                perimter += 1
            if (x-1, y) not in self.outer_coords:
                perimter += 1
        return perimter
    

    def _n_sides(self):
        # return the number of sides of the region
        # a side is a straight line, no matter its length

        all_coords = set(self.coords).union(set(self.outer_coords))

        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        border_cells_by_direction = {d: set() for d in deltas}
        for x, y in all_coords:
            for dx, dy in deltas:
                if (x+dx, y+dy) not in all_coords:
                    border_cells_by_direction[(dx, dy)].add((x, y))
        
        # now border_cells_by_direction contains a set of cells that have a border in the direction of the key
        # now merge all bordering cells that are in the same direction
        # for each direction, merge all bordering cells that are neighbors
        n_sides = 0
        for d, cells in border_cells_by_direction.items():
            merged = set()
            while cells:
                cell = cells.pop()
                merged.add(cell)
                # remove any cells that are connected to this cell
                if d[0] == 1 or d == (-1, 0):
                    direction_to_check = (0, 1)
                else:
                    direction_to_check = (1, 0)
                
                for n in range(1, 100):
                    x = cell[0] + n * direction_to_check[0]
                    y = cell[1] + n * direction_to_check[1]
                    if (x, y) in cells:
                        cells.remove((x, y))
                    else:
                        break
                
                for n in range(1, 100):
                    x = cell[0] - n * direction_to_check[0]
                    y = cell[1] - n * direction_to_check[1]
                    if (x, y) in cells:
                        cells.remove((x, y))
                    else:
                        break
            
                    
        
            n_sides += len(merged)
        return n_sides

    

                    
        
        


    def price(self):
        # size * perimeter
        perimter = self._perimeter()
        return self.size * perimter
    
    def price2(self):
        # size * number of sides
        # each straight line is a side, no matter its length
        sides = self._n_sides()
        return self.size * sides
    

    def belongs_to_region(self, x, y, char):
        # check if the plant at x, y belongs to this region
        if (x+1, y) in self.outer_coords or (x-1, y) in self.outer_coords or (x, y+1) in self.outer_coords or (x, y-1) in self.outer_coords:
            return char == self.char
        return False


    def clean_outer_coords(self):
        # remove coords that are no longer on the outer edge
        for x, y in self.outer_coords:
            if (x+1, y) not in self.outer_coords and (x-1, y) not in self.outer_coords and (x, y+1) not in self.outer_coords and (x, y-1) not in self.outer_coords:
                if len(self.outer_coords) != 1:
                    self.outer_coords.remove((x, y))
        


    def __repr__(self):
        return f"PlantRegion({self.char}, size={self.size}, outer_coords={self.outer_coords})"



regions = []
for char, plants_ in tqdm(plants.items(), total=len(plants), desc="Creating regions"):
    for plant in plants_:
        x, y = plant
        for region in regions:
            if region.belongs_to_region(x, y, char):
                region.size += 1
                region.outer_coords.append((x, y))
                region.coords.append((x, y))
                break
        else:
            regions.append(PlantRegion(char, 1, [plant], [plant]))

print("Created regions, cleaning...")

for region in tqdm(regions, desc="Cleaning regions"):
    region.clean_outer_coords()

print("Regions cleaned, merging...")


# merge regions
def merge_regions(regions: list[PlantRegion]):
    regions_merged = []
    already_merged = []
    for region in tqdm(regions):
        for other_region in regions:
            if other_region in already_merged:
                continue
            if region == other_region:
                continue
            if region.char == other_region.char:
                for x, y in other_region.outer_coords:
                    if region.belongs_to_region(x, y, other_region.char):
                        # merge
                        region.size += other_region.size
                        region.outer_coords.extend(other_region.outer_coords)
                        region.coords.extend(other_region.coords)
                        regions.remove(other_region)
                        already_merged.append(other_region)
                        already_merged.append(region)
                        break
        regions_merged.append(region)
    return regions_merged


for _ in range(10):
    regions = merge_regions(regions)







for region in regions:
    region.clean_outer_coords()
    #print(region.char, region.size, "*", region._perimeter(), "=", region.price(), region._n_sides(), region.price2())



p = sum(region.price() for region in regions)
print(p)


# part 2

p2 = sum(region.price2() for region in regions)
print(p2)
