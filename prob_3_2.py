def sol(MAP):
    visited = {}  # i,j,k

    rows = len(MAP)
    cols = len(MAP[0])

    q= [{0,0,1}]

    while(len(q)>0):
        i,j,k = q.pop(0)

        for act in ((0,1),(0,-1),(-1,0),(1,0)):
            nx, ny = i + act[0], j + act[1]

            if 0 <= nx < rows and 0 <= ny < cols:
                visited[f"{nx},{ny},{k}"] = True
                    

