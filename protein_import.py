from protein import Protein
from parameter import Parameter
import sys

p = Parameter()

prot = Protein(p._('protein.db'))
prot.clear()

id = 0
for line in sys.stdin:
	record = line.strip('\n').split('\t')
	prot.addEntity(
		id,
		[(i,record[i]) for i in range(len(record)) ]
	)
	
	print(record[0])
	
	id += 1

prot.commit()
prot.close()
