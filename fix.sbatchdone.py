import sys
import os
from parameter import Parameter

p = Parameter()

docking_dir = p._('process.prepare.docking_outdir')

for line in sys.stdin:
	cid, pid, dim = line.strip('\n').split('\t')

	dir = docking_dir + '/{}_{}'.format(cid,pid) 
	prepare_grid_file = 'touch {}/prepare_grid.done'.format(dir)


	if os.path.isfile(prepare_grid_file):
		os.system('touch {0}'.format(prepare_grid_file))
		print (cid,pidi, 'prepare_grid.done created')
	else:
		print (cid,pid)
