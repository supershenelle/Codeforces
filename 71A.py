
while True:
    n = input("")
    if n.isdigit() and int(n) in range(1, 101):
        break

text = []
for i in range(int(n)):
    text.append(input(""))

for t in text:
    if len(t) > 10:
        first = t[0]
        last = t[-1]
        count = len(t) - 2
        print(f"{first}{count}{last}")

    else:
        print(t)