a = [12, 3, 1, 2, -6, 5, -8, 6, -2, -1, 4]
b = 18
result = []
a.sort()
for idx, i in enumerate(a[:-3]):
    c = a[idx + 1:]
    for secondary_idx, j in enumerate(c[:-2]):
        sumToFind = b - (i + j)
        left = secondary_idx + 1
        right = len(c) - 1
        while left < right:
            if c[left] + c[right] == sumToFind:
                result.append([i, j, c[left], c[right]])
                left += 1
                right -= 1
            else:
                if c[left] + c[right] > sumToFind:
                    right -= 1
                else:
                    left += 1
if len(result) == 0:
    print(-1)
else:
    print(result)
