import os
import sys
from parameter import Parameter

p = Parameter()

in_dir = p._('process.prepare.compound_indir')
out_dir = p._('process.prepare.compound_outdir')

command = 'prepare_ligand4.py -l {} -o {}'
for id in sys.stdin:
	id = id.strip('\n')
	print(id,'b')

	in_file = '{}/{}.pdb'.format(in_dir,id.lower())
	if not os.path.isfile(in_file):
		continue

	out_mol_dir = '{}/{}'.format(out_dir,id)
	out_file = '{}/{}/molecule.pdbqt'.format(out_dir,id)

	os.system('rm -rf {}'.format(out_mol_dir))
	os.system('mkdir {}'.format(out_mol_dir))
	
	try:
		result = os.system(command.format(in_file, out_file))
		print(id,'e',result)
	except OSError as error:
		print(id,'e', error)

	#print(command.format(in_file, out_file))
	
