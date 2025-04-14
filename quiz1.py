l, h = map(int, input().split())
area = l * h
min_1x3 = float('inf')
for x in range(103):
    if area - 3 * x < 0:
        break
    if (area - 3 * x) % 2 == 0:
        y = (area - 3 * x) // 2
        if y <= 102 and y >= 0:
            min_1x3 = min(min_1x3, x)
print(min_1x3 if min_1x3 != float('inf') else -1)