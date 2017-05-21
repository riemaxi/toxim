from compound import Compound
from parameter import Parameter
import sys

p = Parameter()

cmp = Compound(p._('compound.db'))
freqsave = p.i('compound.freqsave')

field = next(sys.stdin).strip('\n').split('\t')

cmp.clear()
count = 1
for c in sys.stdin:
	c = c.strip('\n').split('\t')
	cmp.addEntity(int(c[0]), [(i,c[i]) for i in range(1,len(c))])
	if count % freqsave == 0:
		cmp.commit()

	print('{}\t{}'.format(count,c[0]))
	count += 1


if count % freqsave != 0:
	cmp.commit()

cmp.close()
