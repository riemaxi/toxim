import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

def adapt_parameter_file(filename):
	params = [
		'autodock_parameter_version',
		'outlev',	
		'intelec',
		'ligand_types',
		'fld',
		'map',
		'elecmap',
		'desolvmap',
		'move',
		'about']

	adapted = ''
	for line in open(filename):
		param = line.split(' ')
		if param[0] in params:
			adapted += line

	adapted += 'epdb'
	with open(filename,'w') as file:
		file.write(adapted)
		

p = Parameter()

proteins = loadProteins(p._('protein.import'))

compound_in_dir = p._('process.prepare.compound_outdir')

out_dir = p._('process.prepare.docking_outdir')

root = os.getcwd()
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
		adapt_parameter_file('ligand_protein.dpf')
		os.chdir(root)

		print('{}\t{}'.format(id,pid))
	
