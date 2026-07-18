import sys

# make FASTA format to dic
dics = {}
cursor = ''
with open(sys.argv[1]) as f:
    for line in f:
         line = line.strip()
         
         if line.startswith('>'):
              cursor = line
              dics[cursor] = ""
         else:
              dics[cursor] += line

complements = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}

DNA1, DNA2 = list(dics.values())
# print(DNA1, DNA2)

transition = 0
transversion = 0
for i in range(len(DNA1)):
    if DNA1[i] == DNA2[i]:
         continue
    elif complements[DNA1[i]] == DNA2[i]:
         transition += 1
    else:
         transversion += 1

print(transition/transversion)




# >Rosalind_0209
# GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
# AGTACGGGCATCAACCCAGTT
# >Rosalind_2200
# TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
# GGTACGAGTGTTCCTTTGGGT

