import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

p = Parameter()

proteins = loadProteins(p._('protein.import'))

compound_in_dir = p._('process.prepare.compound_outdir')

out_dir = p._('process.prepare.docking_outdir')

command = 'prepare_dpf4.py -l ligand.pdbqt -r protein.pdbqt'
for id in sys.stdin:
	id = id.strip('\n').upper()

	compound_in_file = '{}/{}/molecule.pdbqt'.format(compound_in_dir,id)
	
	for pid in proteins:
		pid = pid.upper()
		out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

		os.system('cp {} {}/ligand.pdbqt'.format(compound_in_file,out_mol_dir))

		os.chdir(out_mol_dir)
		os.system(command)
		print('{}\t{}'.format(id,pid))
	
