from parameter import Parameter
from progress import Progress

def print_row(data):
	for cell in data[1:]:
		pid, state = cell.split(':')
		print('{}\t{}\t{}'.format(data[0],pid, state))

p = Parameter()

prg = Progress(p._('progress.db'))
prg.foreach(
	lambda data: print_row(data)
)
prg.close()
