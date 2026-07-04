import sys

dic = {}
cursur = ''
with open(sys.argv[1]) as f:
    for line in f:
         line = line.strip()
         
         if line.startswith('>'):
              cursor = line
              dic[cursor] = ""
         else:
              dic[cursor] += line

n = len(dic[cursor]) 

profile_matrix = {'A': [0]*n, 'C': [0]*n, 'G': [0]*n, 'T': [0]*n}

def counting(strand): 
    for i in range(n):
        profile_matrix[strand[i]][i] += 1
    
for i in dic:
     counting(dic[i])

# print(profile_matrix)

# consussus 만들기
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