def inlt():
    return(list(map(int,input().split())))
def inp():
    return(input())

def move(ins, coord, degree):
    
    if ins == "Forward":
        n_coord = [sum(tup) for tup in zip(coord, hm_move[degree])]
        n_coord = tuple(n_coord)
    else:
        n_degree += hm_dir[ins]
        if abs(n_degree) == 180: n_degree = 180 

    return (n_coord, degree)

def solve(ins_arr, ins_sol, ins, coord, degree, c, target):
    
    if ins_arr == []:
        return (coord == target and c==1)
    
    ins_sol.append(ins_arr[0])
    m = move("Forward", coord, degree)
    s = solve(ins_arr[1:], ins, m[0], m[1], c+1 if "Forward"!=ins_arr[0] else 0, target)
    if s: return True
    m = move("Left", coord, degree)
    s = solve(ins_arr[1:], ins, m[0], m[1], c+1 if "Left"!=ins_arr[0] else 0, target)
    if s: return True
    m = move("Right", coord, degree)
    s = solve(ins_arr[1:], ins, m[0], m[1], c+1 if "Right"!=ins_arr[0] else 0, target)
    return s

degree = 0 # points nord starting from (0,0)
coord = (0,0)
hm_dir = {"Left": -90, "Right": 90}
hm_move = {0: (0, 1), -90: (-1, 0), 90: (1, 0), 180: (0, -1)}
# coord of the target
x, y = inlt()

n = int(inp()) # no of instructions
ins_arr = ["padd"]

for _ in range(n):
    ins = inp()
    ins_arr.append(ins)

ins_sol = ["padd"]
solve(ins_arr, ins_sol, ins, coord, degree, 0, (x,y))

# from 1 4 to 3 2 --> (-2, 2) = (-x,x)
# come up of x "Forward" and change the next instruction
