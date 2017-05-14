import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

p = Parameter()

proteins = loadProteins(p._('protein.import'))

protein_in_dir = p._('process.prepare.protein_outdir')
compound_in_dir = p._('process.prepare.compound_outdir')

out_dir = p._('process.prepare.grid_outdir')

command = 'prepare_gpf4.py -l {0} -r {1}/protein.pdbqt -y -o {1}/protein.gpf'
for id in sys.stdin:
	id = id.strip('\n').upper()

	compound_in_file = '{}/{}/molecule.pdbqt'.format(compound_in_dir,id)
	
	for pid in proteins:
		pid = pid.upper()
		protein_in_file = '{}/{}/molecule.pdbqt'.format(protein_in_dir,pid)
		out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

		os.system('rm -rf {}'.format(out_mol_dir))
		os.system('mkdir {}'.format(out_mol_dir))
		os.system('cp {} {}/protein.pdbqt'.format(protein_in_file,out_mol_dir))

		os.system(command.format(compound_in_file, out_mol_dir))
		print('{}\t{}'.format(id,pid))
	
