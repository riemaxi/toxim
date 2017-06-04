import os
import sys
from parameter import Parameter

p = Parameter()

out_dir = p._('process.prepare.grid_outdir')
root = os.getcwd()

command = 'autogrid4 -p protein.gpf'
count = 1
for pair in sys.stdin:
	id, dim, pid, state = pair.strip('\n').upper().split('\t')

	out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

	os.chdir(out_mol_dir)
	os.system(command)
	os.system('touch create_grid.done')
	os.chdir(root)

	print('{}\t{}\t{}'.format(count,id,pid))

	count += 1
	
