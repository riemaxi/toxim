import sys
from parameter import Parameter
from matrix import Matrix

p = Parameter()
m = Matrix(p._('matrix.db'))
m.clear()

for pair in sys.stdin:
	cid, pid, dim = pair.strip('\n').split('\t')
	m.addScore(cid, dim , '{}:{}'.format(pid,0))
	print(cid, dim, pid)
m.commit()

m.close()
