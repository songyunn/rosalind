import requests
import sys
import re

with open(sys.argv[1]) as f:
    ids = f.readlines()

for id in ids:
    # string을 seq에 저장
    UniProt_id = id.strip().split('_')[0] # strip()를 안해주면 '\n' 이 포함되서 잘못된 답이 나온다.
    raw = requests.get(f'http://www.uniprot.org/uniprot/{UniProt_id}.fasta')
    raw = raw.text.strip().split('\n')
    seq = ''.join(raw[1:])
    
    matches = []
    for i in range(len(seq) - 3): # out of range 방지
         if re.match('N[^P][ST][^P]', seq[i:i+4]): # matches에 index 저장
            matches.append(i+1) # 출력은 파이썬 index 가 아니라 실생활 index로
    
    if len(matches) > 0:
        print(id.strip())
        print(' '.join(str(i) for i in matches))


# N-glycosylation motif -> N{P}[ST]{P}
# -S-, -t-

# [XY] means "either X or Y"
# {X} means "any amino acid except X