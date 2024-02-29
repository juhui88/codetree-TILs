n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dy = [1,0,-1,0]
dx = [0,1,0, -1]

block_num = 0
max_block = 0

max_list = []
def in_range(y,x):
    return 0<=y<n and 0<=x<n

def DFS(y,x, num):
    global block_num, max_block
    max_block += 1
    visited[y][x] = True

    for i in range(4):
        y_move = y + dy[i]
        x_move = x + dx[i]
        if in_range(y_move, x_move) and visited[y_move][x_move] == False and graph[y_move][x_move] == num:
        
            DFS(y_move, x_move, num)


def DFSAll():
    global block_num, max_block
    for y in range(n):
        for x in range(n):
            max_block = 0
            if visited[y][x] == False:
                DFS(y,x,graph[y][x])
                if max_block >= 4:
                    block_num += 1
                    max_list.append(max_block)

DFSAll()
if block_num == 0:
    print(0, 0)
else:
    print(block_num, max(max_list))