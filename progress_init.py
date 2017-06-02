import os
import sys
from parameter import Parameter
from progress import Progress

p = Parameter()
prg = Progress(p._('progress.db'))
prg.clear()

cmp_path = p._('compound.structure') + '/'
excluded = p._('protein.excluded').split(',')

for pair in sys.stdin:
	cid, pid, dim = pair.strip('\n').split('\t')
	if os.path.isfile(cmp_path + cid + '.pdb') and not pid in excluded:
		prg.addState(cid, dim,pid,prg.INITIAL_STATE)
		print(cid, pid, dim)
prg.commit()

prg.close()

print(excluded)
