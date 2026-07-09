import sys

# 코돈 테이블은 그대로 사용
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
 # 위에서 정의하신 테이블

def get_proteins(dna_seq):
    proteins = []
    # 3개씩 묶어 읽는 3개의 시작점(0, 1, 2) 각각에 대해
    for start_pos in range(3):
        # 해당 프레임의 서열
        frame_seq = dna_seq[start_pos:] # 모든 index에서 이렇게 확인하는 것이 더 간단한거 같다.
        
        # 해당 프레임 내의 모든 위치를 조사
        for i in range(0, len(frame_seq) - 2, 3):
            codon = frame_seq[i:i+3]
            
            # 시작 코돈(ATG)을 발견하면 번역 시작
            if codon == 'ATG':
                protein = []
                for j in range(i, len(frame_seq) - 2, 3):
                    sub_codon = frame_seq[j:j+3]
                    aa = dna_codon_table.get(sub_codon)
                    
                    if aa == 'Stop':
                        proteins.append("".join(protein))
                        break
                    elif aa:
                        protein.append(aa)
                    else:
                        break # 3글자가 안 되는 경우 등
    return proteins

# 파일 읽기
with open(sys.argv[1]) as f:
    lines = f.readlines()
    dna = ''.join([line.strip() for line in lines[1:]])

# 정방향과 역보완 서열 생성
def reverse_complement(seq):
    comp = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return "".join([comp[base] for base in seq[::-1]])

dna2 = reverse_complement(dna)

# 결과 수집 (set을 사용하여 중복 자동 제거)
results = set()
results.update(get_proteins(dna))
results.update(get_proteins(dna2))

# 결과 출력
for p in results:
    print(p)