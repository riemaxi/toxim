import sys
from parameter import Parameter
from progress import Progress

p = Parameter()
prg = Progress(p._('test.progress.db'))
prg.clear()

for pair in sys.stdin:
	cid, pid, dim = pair.strip('\n').split('\t')
	prg.addState(cid, dim,pid,prg.GRID_CREATED_STATE)
	print(cid, pid, dim)
prg.commit()

prg.close()
