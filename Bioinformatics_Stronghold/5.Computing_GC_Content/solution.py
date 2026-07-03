import sys

# GC content 계산 함수
def computing_GC(strand):
    C = strand.count('C')
    G = strand.count('G')
    return (C+G)/len(strand)




with open(sys.argv[1]) as f:
    dataset = [line.strip() for line in f.readlines()]

max_GC = 0
max_id = ''

dna_dics = {}
DNA = ''
label = ''

for i in range(len(dataset)):
    if dataset[i][0] == '>':
        if label != '':
            dna_dics[label] = computing_GC(DNA)
        dna_dics[dataset[i]] = 0
        label = dataset[i]
        continue
    DNA.append(dataset[i])
    



# for i in range(0, len(dataset), 2):
#     a = computing_GC(dataset[i+1])
#     if a < max_GC:
#         continue
#     else:
#         max_GC = a
#         max_id = dataset[i]

print(max_id)
print(max_GC*100)







# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT