import sys

def make_profile(n):
    global profile_matrix 
    profile_matrix = {'A': [0]*n, 'C': [0]*n, 'G': [0]*n, 'T': [0]*n}
    
# dna 받으면 counting 하는 함수
def counting(strand, n):
    if 'profile_matrix' not in dir():
        make_profile(n) 
    for i in range(n):
        profile_matrix[strand[i]][i] += 1

strand = []
with open(sys.argv[1]) as f:
    line = f.readline().strip()
    while line:
        if line[0] == '>':
            line = f.readline().strip()
            continue
        else:
            while line[0] != '>':
                strand.append(line)
                line = f.readline().strip()
                if line == '':
                    break
            n = len(strand)
            counting(''.join(strand), n)
            

# consensus 만들기
consensus = ['X']*n
for i in range(n):
    m = max(profile_matrix['A'][i], profile_matrix['C'][i], profile_matrix['G'][i], profile_matrix['T'][i])
    for b in profile_matrix:
        if profile_matrix[b][i] == m:
            consensus[i] = b 

print(''.join(consensus))

for key, values in profile_matrix.items():
    values = ' '.join(str(i) for i in values)
    print(f"{key}: {values}")



# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT