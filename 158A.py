n, k = map(int, input().split())
values = list(map(int, input().split()))

count = 0
set = values[k-1]
for _ in range(n):
    if values[_] >= set and values[_] > 0:
        count += 1

print(count)