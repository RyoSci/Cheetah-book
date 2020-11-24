
memo = [[0 for j in range(6)] for i in range(5)]


def dfs(i, j):
    tmp = 0
    if memo[i][j] != 0:
        return memo[i][j]
    else:
        if i == 4 and j == 5:
            return 1
        elif i == 4:
            tmp += dfs(i, j + 1)
        elif j == 5:
            tmp += dfs(i + 1, j)
        else:
            tmp += dfs(i + 1, j)
            tmp += dfs(i, j + 1)

        memo[i][j] = tmp
        return tmp


print(dfs(0, 0))
for i in range(5):
    print(memo[i])
