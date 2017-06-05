from matrix import Matrix
from parameter import Parameter

def print_row(cid, cells):
	row = '\n'.join(['{}\t{}\t{}'.format(cid,score[0], score[1]) for score in cells])
	print(row)


p = Parameter()
m = Matrix(p._('matrix.db'))

m.foreach(
	lambda data: print_row(data[0][1], data[1:])
)

m.close()
