import sys
import os
from parameter import Parameter

p = Parameter()

for line in sys.stdin:
	org = line.strip('\n')
	dst = org.replace('.sdf','.pdb')
	command = 'obabel -isdf {} -opdb > {}'.format(org, dst)
	os.system(command)
	print(dst)
