t = input()

o = []
for _ in range(int(t)):
    x, y, z = map(int, input().split())
    first = abs(x - y) #pag walang nagtake
    second = (x + z) - y #pag tinake all
    maximum = max(first, second)
    o.append(maximum)

for i in o:
    print(i)