import sys
from compound import Compound
from parameter import Parameter

p = Parameter()

c = Compound(p._('compound.db'))

for pid in sys.stdin:
	pid = pid.strip('\n')
	c.foreach(
		lambda data: print('{}\t{}'.format(data[0][1],pid))
	)
c.close()

