import os
import sys
from parameter import Parameter

def loadProteins(filename):
        with open(filename) as file:
                data = file.read()

        return data.strip('\n').split('\n')

p = Parameter()

proteins = loadProteins(p._('protein.import'))

dir = p._('process.fill_matrix_outdir')
for id in sys.stdin:
	id = id.strip('\n').upper()
	for pid in proteins:
		pid = pid.upper()
		score_file = '{}/{}_{}/scoring.log'.format(dir,id, pid)

		with open(score_file) as file:
			data = file.read().split('\n')[::-1]

		score_line = [s for s in data if 'Estimated Free Energy of Binding' in s]
		score =  score_line[0].split('=',1)[1].split()[0]

		print('{}\t{}\t{}'.format(id,pid, score))

