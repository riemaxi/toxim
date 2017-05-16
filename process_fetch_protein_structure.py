import sys
from parameter import Parameter

import Bio
from Bio.PDB import PDBList

def store(id, dir):
	try:
		pdbl.retrieve_pdb_file(id, pdir='{0}'.format(dir))		
		return 0
	except:
		return 1

p = Parameter()

pdbl = PDBList()

for id in sys.stdin:
	id = id.strip('\n')
	if store(id, p._('process.fetch_protein_structure.store_dir')):
		break
