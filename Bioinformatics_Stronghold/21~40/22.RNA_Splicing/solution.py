import sys

# 파일받기
with open(sys.argv[1]) as f:
    a = f.read().split('>')[1:] # '>'기준으로 split 할시 맨 앞에 ''요소가 list에 들어가서 [1:]로 슬라이싱

# DNA string 얻기
DNA = a[0].splitlines()
DNA = ''.join(DNA[1:])

# print(a)

# introns list 얻기
introns = []
for text in a[1:]:
    string = text.splitlines()[1:]
    introns.append(''.join(string))

# print(introns)

# 슬라이싱 진행
for intron in introns:
    index = DNA.find(intron)
    while index != -1:
        DNA = DNA[:index] + DNA[index+len(intron):]
        # print(DNA)
        index = DNA.find(intron)



dna_codon_table = {
    # T로 시작하는 코돈
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',
    
    # C로 시작하는 코돈
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    
    # A로 시작하는 코돈
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    
    # G로 시작하는 코돈
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

protein = []
# dna를 protein으로 변환
for i in range(0, len(DNA), 3):
    if len(DNA[i:i+3]) < 3:
        continue
    # print(DNA[i:i+3])
    if dna_codon_table[DNA[i:i+3]] == 'Stop':
       break
    protein.append(dna_codon_table[DNA[i:i+3]])

print(''.join(protein))