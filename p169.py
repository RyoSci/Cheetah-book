res = 0


def dfs(x, y):
    global res
    if x == 5 and y == 4:
        res += 1
    elif x == 5:
        dfs(x, y + 1)
    elif y == 4:
        dfs(x + 1, y)
    else:
        dfs(x + 1, y)
        dfs(x, y + 1)


dfs(0, 0)
print(res)
