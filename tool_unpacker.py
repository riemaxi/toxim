import sys
from parameter import Parameter

p = Parameter()

delim = '\t' if p._('tool.packer.del') == 'tab' else p._('tool.packer.del')

for line in sys.stdin:
	for id in line.strip('\n').split(delim):
		print(id)
