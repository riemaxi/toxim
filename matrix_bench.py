from matrix import Matrix
from parameter import Parameter
import sys

def listAll(p,m):
	m.foreach(
		lambda d: print(d),
		p._('matrix_bench.listall.criteria'
	)

def lookup(p,m):
	p._('matrix_bench.lookup.criteria'
	print('look up')

p = Parameter()

matrix = Matrix(p._('matrix.db'))

op = 'list'

{
'list'	: lambda p,m: listAll(p,m),
'lookup': lambda p: lookup(p,m)
}[op](p,matrix)

matrix.close()
