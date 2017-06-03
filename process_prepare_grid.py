import time
import os
import sys
from parameter import Parameter

def prepare_job(template, filename, pdbqtpath, dir):
	tcontent = open(template).read().format(pdbqtpath)
	with open('{}/{}'.format(dir, filename),'w') as file:
		file.write(tcontent)

def holdon(user, process_name):
	locked = True
	print('hold ...')
	while locked:
		os.system('squeue -u {} -n {} > jobs.squeue'.format(user, process_name))
		jobs = open('jobs.squeue').read().strip('\n').split('\n')
		print('# jobs: ', len(jobs) - 1)
		locked = len(jobs)>1

		time.sleep(1)

p = Parameter()

protein_in_dir = p._('process.prepare.protein_outdir')
compound_in_dir = p._('process.prepare.compound_outdir')

out_dir = p._('process.prepare.grid_outdir')

root = os.getcwd()
user = p._('user')
process_name = 'prepare_grid_job.sh'

command = 'sbatch prepare_grid_job.sh'
count = 1
payload = p.i('process.prepare.grid_payload')
for pair in sys.stdin:
	if count % payload == 0:
		holdon(user, process_name)

	id, dim, pid, state = pair.strip('\n').upper().split('\t')

	protein_in_file = os.path.abspath( '{}/{}/molecule.pdbqt'.format(protein_in_dir,pid) )
	out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

	os.system('rm -rf {}'.format(out_mol_dir))
	os.system('mkdir {}'.format(out_mol_dir))
	os.system('cp {} {}/protein.pdbqt'.format(protein_in_file,out_mol_dir))
	prepare_job('template/prepare_grid_job.sh','prepare_grid_job.sh', protein_in_file, out_mol_dir)
	
	os.chdir(out_mol_dir)
	os.system(command)
	os.chdir(root)

	print('{}\t{}\t{}'.format(count,id,pid))

	count += 1
