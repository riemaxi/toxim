from parameter import Parameter
from progress import Progress
import os

def print_row(cid, data, dir, count):
	for cell in data:
		pid, state = cell[1].split(':')
		if not os.path.isfile('{}/{}_{}/prepare_grid.done'.format(dir, cid, pid)):
			print('{}\t{}\t{}\t{}\t{}'.format(cid,cell[0],pid, state, count[0]))
		count[0]+=1

p = Parameter()

prg = Progress(p._('progress.db'))
dock_dir = p._('process.prepare.docking_outdir')

count = [1]
prg.foreach(
	lambda cid, data: print_row(cid, data, dock_dir, count)
)
prg.close()
