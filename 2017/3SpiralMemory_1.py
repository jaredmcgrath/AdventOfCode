import math
# For this problem, note that the bottom right corner of every square is the square of an odd number
x = 325489
n = 1
while x / n**2 >= 1:
    n += 2
# After deducing the side length of the square, n, working our way back to the origin is trivial
offset = x % n
# ceil(n/2) travels half of the perimeter, rounded up, to the left
# ceil(n/2) - offset - 1 travels the remainder of the distance up
ans = math.ceil(n/2) + (math.ceil(n/2) - offset - 1)
print(ans)
