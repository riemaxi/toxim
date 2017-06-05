import os
import sys
from parameter import Parameter
from processholder import ProcessHolder

JOB_NAME = 'create_grid_job.sh'

p = Parameter()
holder = ProcessHolder(p._('user'),JOB_NAME)

out_dir = p._('process.prepare.grid_outdir')
root = os.getcwd()

template = open('template/' + JOB_NAME).read()

command = 'sbatch ' + JOB_NAME
payload = p.i('process.sbatch.payload')
for pair in sys.stdin:
	id, dim, pid, state, count = pair.strip('\n').upper().split('\t')

	if count % payload == 0:
		print('hold ...')
		holder.hold()

	out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)
	holder.prepare(template, out_mol_dir)

	os.chdir(out_mol_dir)
	os.system(command)
	os.chdir(root)

	print('{}\t{}\t{}'.format(count,id,pid))
	
