a = [12, 3, 1, 2, -6, 5, -8, 6, -2, -1]
b = 3
result = []
a.sort()
left, right = 0, len(a) - 1
while left < right:
    if a[left] + a[right] == b:
        result.append([a[left], a[right]])
        left += 1
        right -= 1
    else:
        if a[left] + a[right] > b:
            right -= 1
        else:
            left += 1
if len(result) == 0:
    print(-1)
else:
    print(result)
