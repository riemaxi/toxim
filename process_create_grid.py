import os
import sys
from parameter import Parameter
from process.holder import ProcessHolder

JOB_NAME = 'create_grid_job.sh'

p = Parameter()
holder = ProcessHolder(p._('user'),JOB_NANE, 'template/' + JOB_NAME)

out_dir = p._('process.prepare.grid_outdir')
root = os.getcwd()

template = open('template/' + JOB_NAME).read()

command = 'sbatch ' + JOB_NAME
count = 1
payload = p.i('process.sbatch.payload')
for pair in sys.stdin:
	if count % payload == 0:
		holder.hold()
		
	id, dim, pid, state = pair.strip('\n').upper().split('\t')

	out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)
	holder.prepare(template)

	os.chdir(out_mol_dir)
	os.system(command)
	os.chdir(root)

	print('{}\t{}\t{}'.format(count,id,pid))

	count += 1
	
