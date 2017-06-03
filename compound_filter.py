import sys
import os
from parameter import Parameter

p = Parameter()

excluded = p._('compound_filter.excluded').split(',')
cmp_path = p._('compound.structure') + '/'

for cid in sys.stdin:
	cid = cid.strip('\n')
	if cid in excluded or not os.path.isfile(cmp_path + cid + '.pdb'):
		continue
	
	print(cid)
