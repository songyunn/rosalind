import sys

with open(sys.argv[1]) as f:
    a = f.read().strip().splitlines()
    dna = ''.join(a[1:])

complement_table = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def check(i, e, n, string):
    if i-1 < 0 or e+1 >= len(string):
        return(i,n)
    if complement_table[string[i-1]] == string[e+1]:
        # 6개 string에서 그 사이에 있는 4개도 출력하기 위해 추가
        if n >=4 and n <=12:
            print(i+1, n)
        return(check(i-1, e+1, n+2, string))
    elif complement_table[string[i-1]] != string[e+1]:
        return(i, n)


for i in range(len(dna)-1): #마지막 문자는 확인 필요 X
    if complement_table[dna[i]] == dna[i+1]:
        # 옆에를 계속 확인하는 recursion
        index, n = check(i, i+1, 2, dna)
        if n >= 4 and n <= 12:
            print(index+1, n)
