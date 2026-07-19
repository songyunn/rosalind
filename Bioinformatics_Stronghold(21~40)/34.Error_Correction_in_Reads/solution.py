import sys

dic = {}
cursor = ''
with open(sys.argv[1]) as f:
    for line in f:
         line = line.strip()
         
         if line.startswith('>'):
              cursor = line
              dic[cursor] = ""
         else:
              dic[cursor] += line

def hamming_dis(string1, string2):

    # 출력값 초기화
    Hamming_distance = 0

    # DNA1 DNA2 비교하기
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            Hamming_distance += 1

    return(Hamming_distance)

# reverse complement로 변환하는 함수
def reverse_complement(string):
    # complement 표를 생성 후에 이를 for문으로 적용
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    string = string[::-1]
    output = []

    for i in range(len(string)):
        output.append(complement[string[i]])

    return(''.join(output))  

reads = list(dic.values()) # 모든 read 데이터

i = 0
normal = []
error = []
while True:
    if len(reads) == 0:
        break
    temp = reads[0]
    reads = reads[1:]

    a = [a for a in range(len(reads)) if reads[a] == temp] # cursor와 동일한 index 모두 뽑기
    count = 0
    for i in a:
        normal.append(reads[i-count])
        del reads[i-count]
        count += 1

    b = [a for a in range(len(reads)) if reads[a] == reverse_complement(temp)]
    count = 0
    for i in b:
        normal.append(reads[i-count])
        del reads[i-count]
        count += 1

    if len(a) == 0 and len(b) == 0:
        error.append(temp)
    else:
        normal.append(temp)

# --------------------------- 오류 수정하기 ------------------------------- #

for i in error:
    for j in normal:
        if hamming_dis(i,j) == 1:
            print(i+'->'+j)
            break
        elif hamming_dis(reverse_complement(i), j) == 1:
            print(i+'->'+reverse_complement(j))
            break

# >Rosalind_52
# TCATC
# >Rosalind_44
# TTCAT
# >Rosalind_68
# TCATC
# >Rosalind_28
# TGAAA
# >Rosalind_95
# GAGGA
# >Rosalind_66
# TTTCA
# >Rosalind_33
# ATCAA
# >Rosalind_21
# TTGAT
# >Rosalind_18
# TTTCC