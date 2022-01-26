from itertools import accumulate
import sys

input = sys.stdin.readline


def add_tiles(maze, x, y):
    global count
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    elif maze[x][y] == "I" or maze[x][y] == "X":
        return False
    else:
        maze[x][y] = "X"
        count += 1
        if (
            add_tiles(maze,x, y - 1)
            or add_tiles(maze, x, y + 1)
            or add_tiles(maze, x - 1, y)
            or add_tiles(maze, x + 1, y)
        ):
            return True
    return False


num_tiles = int(input())
r = int(input())
c = int(input())

floor_plan = []

for _ in range(r):
    floor_plan.append(list(input().strip()))


counts = []
for i in range(r):
    for j in range(c):
        if floor_plan[i][j] == ".":
            count = 0
            add_tiles(floor_plan, i, j)
            counts.append(count)

sorted_counts = sorted(counts, reverse=True)

total_tiles = list(accumulate(sorted_counts))


for i in range(len(total_tiles)):
    if total_tiles[i] > num_tiles:
        if i > 1:
            print("{} rooms, {} square metre(s) left over".format(i, num_tiles - total_tiles[i - 1]))
            break
        if i == 1:
            print("{} room, {} square metre(s) left over".format(i, num_tiles - total_tiles[i - 1]))
        else:
            print("{} rooms, {} square metre(s) left over".format(i, num_tiles))
            break

if total_tiles[-1] <= num_tiles:
    print("{} rooms, {} square metre(s) left over".format(len(total_tiles), num_tiles - total_tiles[-1]))
