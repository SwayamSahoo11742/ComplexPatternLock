import math
import random 
from animate import draw_pattern_animation
coords = [(0,2), (1,2), (2,2), (0,1), (1,1), (2,1), (0,0), (1,0), (2,0)]

def get_all_sols(grid_size: (int, int), max_len: int) -> list:
    """
    Return all solutions to the android problem as a list
    :param grid_size: (x, y) size of the grid
    :param max_len: maximum number of nodes in the solution
    """
    sols = []

    def r_sols(current_sol):
        current_y = current_sol[-1] 
        current_x = current_sol[-1] - current_y * grid_size[1]  
        grid = {} 
        grid_id = -1

        for y in range(grid_size[1]):
            for x in range(grid_size[0]):
                grid_id += 1
                if grid_id in current_sol:  
                    continue
                dist = (x - current_x) ** 2 + (y - current_y) ** 2  
                slope = math.atan2((y - current_y), (x - current_x))  

                grid[slope] = (dist, grid_id) if grid.get(slope) is None or grid[slope][0] > dist else grid[slope]

        r_sol = [current_sol]
        if len(current_sol) == max_len: 
            return r_sol

        for _, opt in grid.values(): 
            r_sol += r_sols(current_sol + [opt])
        return r_sol

    for start in range(grid_size[0] * grid_size[1]):
        sols += r_sols([start])
    return sols

pats = (get_all_sols((3,3), 9))

def filter_lists_by_length(lists, x):
    return [lst for lst in lists if len(lst) == x]

pats = filter_lists_by_length(pats, 9)

def conv(lst:list):
    n = lst.copy()
    for i in range(9):
        n[i] = coords[n[i]]
    return n

def slope(p1:tuple,p2:tuple):
    if p1[0]-p2[0]:
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
    else:
        m = 999
    return m

complex = []
for pat in pats:
    slopes = set()
    coord_pat = conv(pat)
    for i in range(8):
        slopes.add(slope(coord_pat[i], coord_pat[i+1]))
    if(len(slopes)) == 8:
        complex.append(pat)

rand_pat = conv(random.choice(complex))

draw_pattern_animation(rand_pat, xlim=(3,-1), ylim=(3,-1), num_frames=50, interval=50)