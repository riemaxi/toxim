import os
import sys
from parameter import Parameter

p = Parameter()

in_dir = p._('process.prepare.protein_indir')
out_dir = p._('process.prepare.protein_outdir')

os.system('rm -rf {}/*'.format(out_dir))

command = 'obabel -ipdb {} -opdbqt > {}'
for id in sys.stdin:
	id = id.strip('\n')

	in_file = '{}/{}.pdb'.format(in_dir,id.lower())

	out_mol_dir = '{}/{}'.format(out_dir,id)
	out_file = '{}/{}/molecule.pdbqt'.format(out_dir,id)
	os.system('mkdir {}'.format(out_mol_dir))

	os.system(command.format(in_file, out_file))
	print(id)
