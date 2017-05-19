from parameter import Parameter
from compound import Compound
import os

def check(cid, c, dir):
	optimized = os.path.isfile('{}/{}_3d.pdb'.format(dir,cid))
	c.addValue(cid,c.INCHI + 1,optimized)
	
	if optimized:
		print(cid)
	
	

p = Parameter()

dir = p._('compound.optimize.structure')

structure = p._('compound.fetch.structure')
c = Compound(p._('compound.db'))
c.listAll( lambda data: check(data[1],c, dir) )
c.commit()
c.close()

