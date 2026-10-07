n = int(input())

for _ in range(n):
    n = int(input())
    a = list(map(int, input().split()))

    m = n - 4
    values = []

    for x in range(m):
        value = a[x] + a[x + 2] - a[x + 4]
        values.append(value)

    freq = {}

    for i in values:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1

    answer = 0

    for i in freq:
        count = freq[i]
        answer += count * (count - 1) // 2

    for x in range(m):
        if x + 2 < m and values[x] == values[x + 2]:
            answer -= 1

        if x + 4 < m and values[x] == values[x + 4]:
            answer -= 1

    print(answer)