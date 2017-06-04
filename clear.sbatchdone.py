import sys
import os
from parameter import Parameter

p = Parameter()

docking_dir = p._('process.prepare.docking_outdir')

for line in sys.stdin:
	cid, pid, dim = line.strip('\n').split('\t')

	dir = docking_dir + '/{}_{}'.format(cid,pid) 
	create_grid_file = 'rm {}/create_grid.done'.format(dir)


	if os.path.isfile(create_grid_file):
		os.system('rm {0}'.format(create_grid_file))
		print (cid,pid, 'create_grid.done removed')
	else:
		print (cid,pid)

