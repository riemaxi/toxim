import sys
import os
from parameter import Parameter

def optimize(path, dest, format):
	command = 'obminimize -ff {3} -sd -c 1e-5 -o {0} {1} > {2}'.format(format, path, dest, ff)
	os.system(command)

p = Parameter()

out = p._('compound.optimize.structure')
format = p._('compound.optimize.format','pdb')

for path in sys.stdin:
	path = path.strip('\n')
	entry = path.split('/')
	file = entry[len(entry)-1].replace('_2d','_3d').split('.')
	file = '.'.join(file[:len(file)-1])
	optimize(path,'{}/{}.{}'.format(out,file,format), format)
