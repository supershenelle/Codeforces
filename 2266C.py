t = input()
o = []

for _ in range(int(t)):
    n = int(input())
    num = input()
    sortednum = "".join(sorted(num))

    if num == sortednum:
        o.append(0)
        continue

    zeros = num.count("0")

    if num[0] == "1": 
        o.append(zeros)

    elif num[0] == "0":
        onesleft = 0
        zerosright = zeros
        minimum = zeros

        for i in num:
            if i == "1":
                onesleft += 1

            elif i == "0":
                zerosright -= 1

            minimum = min(minimum, onesleft + zerosright)

        o.append(minimum)

for i in o:
    print(i)
    