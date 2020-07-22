import copy
n = 2 #int(input())
east = 0.01 * 25 #int(input())
west = 0.01 * 25 #int(input())
south = 0.01 * 25 #int(input())
north = 0.01 * 25 #int(input())

n = int(input())
east = 0.01 * int(input())
west = 0.01 * int(input())
south = 0.01 * int(input())
north = 0.01 * int(input())

position = (0, 0)
have_passed_set = set()
have_passed_set.add(position)
tmp_possibilities = 1
sum_possibilities = 0
def dfs(i, position, have_passed_set, tmp_possibilities):
    global sum_possibilities
    #終了条件 最後のノード
    if i == n:
        sum_possibilities += tmp_possibilities
        return True

    #初期化  
    tmp_set = copy.copy(have_passed_set) #setに関しては各方面の前にも初期化を行う必要がある。
    x, y = position

    #east
    tmp_set = copy.copy(have_passed_set)
    tmp_position = (x + 1, y)
    if tmp_position not in tmp_set:
        tmp_set.add(tmp_position)
        dfs(i + 1, tmp_position, tmp_set, tmp_possibilities * east)

    #west
    tmp_set = copy.copy(have_passed_set)
    tmp_position = (x - 1, y)
    if tmp_position not in tmp_set:
        tmp_set.add(tmp_position)
        dfs(i + 1, tmp_position, tmp_set, tmp_possibilities * west)

    #south
    tmp_set = copy.copy(have_passed_set)
    tmp_position = (x, y - 1)
    if tmp_position not in tmp_set:
        tmp_set.add(tmp_position)
        dfs(i + 1, tmp_position, tmp_set, tmp_possibilities * south)

    #north
    tmp_set = copy.copy(have_passed_set)
    tmp_position = (x, y + 1)
    if tmp_position not in tmp_set:
        tmp_set.add(tmp_position)
        dfs(i + 1, tmp_position, tmp_set, tmp_possibilities * north)

dfs(0, position, have_passed_set, tmp_possibilities)
print(sum_possibilities)