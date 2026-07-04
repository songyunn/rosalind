dna = input()
dna_sub = input()
n = len(dna_sub)
output = []

for i in range(0, len(dna)):
    if len(dna) <= i+n:
        break
    if dna[i:i+n] == dna_sub:
        output.append(i+1)

print(' '.join(str(i) for i in output))