while True:
    w = input("")
    if w.isdigit():
        w = int(w)
        if w in range (1, 101):
            break

if w > 2 and w % 2 == 0:
    print("YES")

else:
    print("NO")