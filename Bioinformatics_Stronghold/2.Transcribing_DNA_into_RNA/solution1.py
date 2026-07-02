import sys

DNA = open(sys.argv[1]).read()
RNA = DNA.replace('T', 'U')

print(RNA)