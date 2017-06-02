import sys
from parameter import Parameter
from progress import Progress

p = Parameter()
prg = Progress(p._('test.progress.db'))

prg.foreach(
	lambda data: print('\t'.join([str(v) for v in data])),
	'e.dimension < 11'
)

prg.close()
