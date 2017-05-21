import sys
from matrix import Matrix
from parameter import Parameter

p = Parameter()

m = Matrix(p._('matrix.db'))
m.foreach(
	lambda data: print(data[0][1])
)
m.close()
