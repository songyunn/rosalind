import sys

# make FASTA format to dic
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

n = len(dic[cursor])
