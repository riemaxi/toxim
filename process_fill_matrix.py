import random
import os
import sys
from parameter import Parameter
from matrix import Matrix

def score(cid, dim,dir):
	score_file = '{}/{}_{}/scoring.log'.format(dir,cid, dim)

	try:
		with open(score_file) as file:
			data = file.read().split('\n')[::-1]

		score_line = [s for s in data if 'Estimated Free Energy of Binding' in s]
		score =  score_line[0].split('=',1)[1].split()[0]

		return score
	except:
		random.seed()
		return random.random()	

p = Parameter()
m = Matrix(p._('matrix.db'))

dir = p._('process.fill_matrix_outdir')

for tpl in sys.stdin:
	cid,pid, dim = tpl.strip('\n').split('\t')
	scr = score(cid,dim,dir)
	m.addScore(cid,dim, scr)
	print('{}\t{}\t{}\t{}'.format(cid,pid,dim,scr))

m.commit()
