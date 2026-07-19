import sys

with open(sys.argv[1]) as f:
    nodes = f.readline()
    adj_list = f.readlines()

n = len(adj_list)

print(int(nodes) - n - 1)