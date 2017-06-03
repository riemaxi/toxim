from parameter import Parameter
from progress import Progress

def print_row(cid, data):
	for cell in data:
		pid, state = cell[1].split(':')
		print('{}\t{}\t{}\t{}'.format(cid,cell[0],pid, state))

p = Parameter()

prg = Progress(p._('progress.db'))
prg.foreach(
	lambda cid, data: print_row(cid, data)
)
prg.close()
