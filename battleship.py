from collections import defaultdict

def solution(grid, shots):
    dict = defaultdict(list)
    already_attacked = set()
    
    result = []
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            dict[grid[row][col]].append([row, col])
            
    for key, values in dict.items():
        dict[key] = sorted(values)
            
    for shot in shots:
        print(f"shot: {shot}")
        x_coord = shot[0]
        y_coord = shot[1]
        
        if grid[x_coord][y_coord] == ".":
            result.append("Missed")
            print("Missed")
        else:
            ship = grid[x_coord][y_coord]
            print(f"ship: {ship}")
            if (x_coord, y_coord) in already_attacked:
                result.append("Already attacked")
                print(f"Already Attacked")
            elif [x_coord, y_coord] in dict[ship] and len(dict[ship]) > 1:
                print(f"ship: {ship} dict[ship][-1]: {dict[ship][-1]} and [x_coord, y_coord]: {[x_coord, y_coord]}")
                result.append(f"Attacked Ship {ship}")
                dict[ship].remove([x_coord, y_coord])
                already_attacked.add((x_coord, y_coord))
            else:
                result.append(f"Ship {ship} sunk")
                already_attacked.add((x_coord, y_coord))
                
    return result
        

# Example grid and shots
grid = [
    [".", "A", "B", "B", "B"],
    [".", "A", ".", ".", "C"],
    [".", ".", ".", ".", "."],
    ["D", "D", ".", ".", "."],
    [".", "E", "E", "E", "E"]
]
shots = [
    [0, 0], [0, 1], [0, 2], [1, 1], [0, 1],
    [1, 4], [2, 2], [2, 4], [0, 3], [0, 0], [0, 4]
]

grid = [
    [".", ".", "B", "B", "B"],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

shots = [[0,0],[0,0],[0,4],[0,4]]

grid = [
    [".", "A", "B", "B", "B"],
    [".", "A", ".", ".", "C"],
    [".", ".", ".", ".", "."],
    ["D", "D", ".", ".", "."],
    [".", "E", "E", "E", "E"]
]
shots = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
    [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
    [1, 1], [1, 1], [0, 0], [4, 4]
]

output = solution(grid, shots)
print(output)

#  [“Missed”, “Attacked ship A”, “Attacked ship B”, “Ship A sunk”, “Already attacked”, “Ship C sunk”, “Missed”, “Attacked ship B”, “Missed”, “Ship B sunk”]
