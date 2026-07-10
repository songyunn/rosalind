# request 라이브러리 사용
import requests

a = requests.get('http://www.uniprot.org/uniprot/B5ZC00.fasta')
a = a.text.strip().split('\n')

print(''.join(a[1:]))
  
