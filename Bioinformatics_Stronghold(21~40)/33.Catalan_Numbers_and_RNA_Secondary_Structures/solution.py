import sys

with open(sys.argv[1]) as f:
    RNA = ''.join(f.read().splitlines()[1:])

memo = {}
complement_table ={'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}

def RNA_catalan(string):
    # 남은 string이 없다면 마지막까지 짝을 찾았기 때문에 reuturn 1
    if len(string) == 0:
        return 1

    if string in memo:
        return memo[string]

    # 너무 느려서 조건 추가
    if string.count('A') != string.count('U') or string.count('C') != string.count('G'):
        return 0

    a = complement_table[string[0]]
    result = [i for i in range(len(string)) if string[i]== a and (i+1)%2 == 0] # 짝지을 수 있는 경우의 수
    print(string, result)
    # result 가 없다면 가능한 경우의 수가 없기 때문에 return 0
    if len(result) == 0:
        return 0

    output = 0
    for i in result:
        output += RNA_catalan(string[1:i]) * RNA_catalan(string[i+1:])
    
    memo[string] = output
    return output % 1000000

print(RNA_catalan(RNA))