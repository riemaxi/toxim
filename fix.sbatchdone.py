import sys
import os
from parameter import Parameter

p = Parameter()

docking_dir = p._('process.prepare.docking_outdir')

for line in sys.stdin:
	cid, pid, dim = line.strip('\n').split('\t')

	dir = docking_dir + '/{}_{}'.format(cid,pid) 
	file = 'touch {}/prepare_grid.done'.format(dir)


	if os.path.isdir(dir):
		os.system('touch {0}'.format(file))
		print (pid,dim)
