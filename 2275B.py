t = int(input())

for _ in range(t):
    documents = int(input())
    string = input()

    memory = []
    printed = [False] * (documents + 1)

    for i in range(1, documents + 1):

        command = string[i - 1]

        if command == '1':
            memory.append(i)

        elif command == '2':
            if memory:
                doc = memory.pop()
                printed[doc] = True
            else:
                printed[i] = True

        else:
            printed[i] = True

    answer = []

    for i in range(1, documents + 1):
        if not printed[i]:
            answer.append(i)

    print(len(answer))
    print(*answer)