a = [12, 3, 1, 2, -6, 5, -8, 6, -2, -1]
b = 3
result = []
a.sort()
for idx, i in enumerate(a[:-3]):
    sumToFind = b - i
    left = idx + 1
    right = len(a) - 1
    while left < right:
        if a[left] + a[right] == sumToFind:
            temp = [i, a[left], a[right]]
            result.append(temp)
            left += 1;
            right -= 1;
        else:
            if a[left] + a[right] > sumToFind:
                right -= 1;
            else:
                left += 1;
if len(result) == 0:
    print(-1)
else:
    print(result)
