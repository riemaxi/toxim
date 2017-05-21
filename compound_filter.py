import sys
from parameter import Parameter

p = Parameter()

excluded = p._('compound_filter.excluded').split(',')

for cid in sys.stdin:
	cid = cid.strip('\n')
	if cid in excluded:
		continue
	
	print(cid)
