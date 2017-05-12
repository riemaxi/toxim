from matrix import Matrix
from parameter import Parameter
import sys

def loadProteins(filename):
	with open(filename) as file:
		data = file.read()

	return data.strip('\n').split('\n')

p = Parameter()

proteins = loadProteins(p._('protein.import'))

matrix = Matrix(p._('matrix.db'))
matrix.clear()

id = 0
for cid in sys.stdin:
	cid = cid.strip('\n')
	for pid in proteins:
		matrix.addScore(id,cid,pid)

	print(cid)
	id += 1

matrix.commit()
matrix.close()
