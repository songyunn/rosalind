import sys

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

# 3.complementing a strand of dna 코드 사용
def reverse_dna(dna):
     dna = dna[::-1]
     output = []
     # complement 표를 생성 후에 이를 for문으로 적용
     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

     for i in range(len(dna)):
         output.append(complement[dna[i]])

     return(''.join(output))  

# 파일 읽기
with open(sys.argv[1]) as f:
     a = f.read()

# dna1과 역 dna 갖고오기
dna = ''.join(a.splitlines()[1:])
dna2 = reverse_dna(dna)

# 총 6개의 dna reading frames 만들기
dna_reading_frames = []
for i in range(3):
     dna_reading_frames.append(dna[i:])
     dna_reading_frames.append(dna2[i:])

# string에서 시작 코돈 발견되면 기록 시작, end codon 나오면 print

# record가 for문 밖에 있어서 문제가 발생했었음
output_record = []
for string in dna_reading_frames:
     record = False
     for i in range(0, len(string), 3):
          if dna_codon_table.get(string[i:i+3]) == None:
               break
          if record == False:
               if dna_codon_table.get(string[i:i+3]) == 'M': # .get()을 사용하여 key값이 없더라도 None 반환
                    protein_string = ['M']
                    record = True
                    continue
          if record == True:
               a = dna_codon_table.get(string[i:i+3])
               if a != "Stop":
                    protein_string.append(a)
               elif a == "Stop":
                    output = ''.join(protein_string)
                    #record = False가 if 안에 있어서 문제가 발생했었음
                    record = False 

                    # 같은 output이 나오는것을 방지
                    if output not in output_record:
                         print(output)
                         output_record.append(''.join(protein_string))
                         
for output in output_record:
     if 'M' in output[1:]:
          M_index = output[1:].find('M') + 1 # [1:0]으로 슬라이싱 했기 때문에 +1을 해준다.
          if output[M_index:] not in output_record:
               print(output[M_index:])
               output_record.append(output[M_index:])