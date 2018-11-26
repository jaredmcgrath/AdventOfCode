# Pro-tip: don't spend 2 hours over thinking it when you can just simulate it and print out the result

target = 325489


def surrounding_sum(x_0, y_0, array_2d):
    total = 0
    total += array_2d[y_0][x_0+1]
    total += array_2d[y_0+1][x_0+1]
    total += array_2d[y_0+1][x_0]
    total += array_2d[y_0+1][x_0-1]
    total += array_2d[y_0][x_0-1]
    total += array_2d[y_0-1][x_0-1]
    total += array_2d[y_0-1][x_0]
    total += array_2d[y_0-1][x_0+1]

    return total


arr = [[0 for i in range(100)] for j in range(100)]
arr[50][50] = 1
arr[50][51] = 1
x = 51
y = 50
next_sum = 0
while next_sum < target:
    # Move up until there is nothing to the left
    while arr[y][x-1] != 0 and next_sum < target:
        y += 1
        next_sum = surrounding_sum(x, y, arr)
        arr[y][x] = next_sum
    # Move left until there is nothing below
    while arr[y-1][x] != 0 and next_sum < target:
        x -= 1
        next_sum = surrounding_sum(x, y, arr)
        arr[y][x] = next_sum
    # Move down until there is nothing to the right
    while arr[y][x+1] != 0 and next_sum < target:
        y -= 1
        next_sum = surrounding_sum(x, y, arr)
        arr[y][x] = next_sum
    # Move right until there is nothing above
    while arr[y+1][x] != 0 and next_sum < target:
        x += 1
        next_sum = surrounding_sum(x, y, arr)
        arr[y][x] = next_sum

print(next_sum)
