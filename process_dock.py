import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

def prepare_parameters(tcontent):
	pcontent = open('ligand_protein.dpf').read()
	with open('ligand_protein.dpf','w') as file:
		file.write('{}\n{}'.format(pcontent, tcontent))


p = Parameter()

proteins = loadProteins(p._('protein.import'))

compound_in_dir = p._('process.prepare.compound_outdir')

out_dir = p._('process.prepare.docking_outdir')

template = open(p._('process.dock.search_params')).read()

root = os.getcwd()
command = 'autodock4 -p ligand_protein.dpf -l scoring.log'
for id in sys.stdin:
	id = id.strip('\n').upper()
	
	for pid in proteins:
		pid = pid.upper()
		out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

		os.chdir(out_mol_dir)
		prepare_parameters(template)

		os.system(command)
		os.chdir(root)

		print('{}\t{}'.format(id,pid))

