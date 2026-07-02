data = input()

A, C, G, T = 0, 0, 0, 0

for i in range(len(data)):
    if data[i] == 'A':
        A += 1
    elif data[i] == 'C':
        C += 1
    elif data[i] == 'G':
        G += 1
    elif data[i] == 'T':
        T += 1

print(A, C, G, T)