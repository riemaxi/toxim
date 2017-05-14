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

initdir = os.getcwd()

command = 'autogrid4 -p {}'
for id in sys.stdin:
	id = id.strip('\n').upper()

	for pid in proteins:
		pid = pid.upper()

		out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

		protein_in_file = os.path.abspath('{}/{}/molecule.pdbqt'.format(protein_in_dir,pid))
		param_file = 'molecule.gpf'

		os.system('cp {} .'.format(protein_in_file))

		os.system('cd {}'.format(out_mol_dir))
		#os.system(command.format(param_file))
		print('{}\t{}'.format(id,pid))

		os.system('cd {}'.format(initdir))

		print(command.format(param_file))
	
