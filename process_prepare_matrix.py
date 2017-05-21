import sys
from matrix import Matrix
from parameter import Parameter

p = Parameter()

excluded = p._('process.prepare_matrix.excluded').split(',')

m = Matrix(p._('matrix.db'))
m.clear()
count = 1
for cid in sys.stdin:
	cid = cid.strip('\n').split('/')[-1].replace('.pdb','')

	if cid in excluded:
		continue

	m.addCompound(cid)
	print('{}\t{}'.format(count,cid))
	
	count += 1

m.commit()
m.close()
