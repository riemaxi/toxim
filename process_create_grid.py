import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

p = Parameter()

proteins = loadProteins(p._('protein.import'))

out_dir = p._('process.prepare.grid_outdir')
root = os.getcwd()

command = 'autogrid4 -p protein.gpf'
for id in sys.stdin:
	id = id.strip('\n').upper()

	for pid in proteins:
		pid = pid.upper()

		out_mol_dir = '{}/{}_{}'.format(out_dir,id, pid)

		os.chdir(out_mol_dir)
		os.system(command)
		os.chdir(root)

		print('{}\t{}'.format(id,pid))

		#print(command.format(param_file))
	
