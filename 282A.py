n = input()

count = 0
for _ in range(int(n)):
    text = input()
    if text == "X++" or text == "++X":
        count += 1

    elif text == "X--" or text == "--X":
        count -= 1

print(count)