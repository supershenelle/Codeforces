t = input()

o = []
for _ in range(int(t)):
    n = int(input())
    x, y, z = map(int, input().split())
    minimum = min(x, y, z)
    output = n - minimum
    o.append(output)

for i in o:
    print(i)