import os
import sys
from parameter import Parameter

p = Parameter()

in_dir = p._('process.prepare.compound_indir')
out_dir = p._('process.prepare.compound_outdir')

os.system('rm -rf {}/*'.format(out_dir))

command = 'prepare_ligand4.py -l {} -o {}'
for id in sys.stdin:
	id = id.strip('\n')

	in_file = '{}/{}_3d.pdb'.format(in_dir,id.lower())

	out_mol_dir = '{}/{}'.format(out_dir,id)
	out_file = '{}/{}/molecule.pdbqt'.format(out_dir,id)
	
	os.system('mkdir {}'.format(out_mol_dir))

	os.system(command.format(in_file, out_file))
	print(id)

	#print(command.format(in_file, out_file))
	
