n = int(input())

for i in range(n):
    x, y, r = map(int, input().split())
    print(f"{x + r} {y}")