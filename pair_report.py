import os
import sys
from compound import Compound
from parameter import Parameter

def print_pair(cid, pid, comp_dir, excluded):
	cid = str(cid)
	file = comp_dir + cid + '.pdb'
	if (os.path.isfile(file) and (cid not in excluded)):
		print('{}\t{}'.format(cid,pid))
	

p = Parameter()

c = Compound(p._('compound.db'))
comp_dir = p._('compound.structure') + '/'
excluded = p._('compound_filter.excluded').split(',')

for pid in sys.stdin:
	pid = pid.strip('\n')
	c.foreach(
		lambda data: print_pair(data[0][1], pid, comp_dir, excluded)
	)
c.close()
