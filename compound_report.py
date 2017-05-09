from parameter import Parameter
from compound import Compound

p = Parameter()

structure = p._('compound.fetch.structure')
c = Compound(p._('compound.db'))
c.listAll( lambda data: print('{},{},{}/{}.{}'.format(data[0], data[1], structure, data[0],'sdf') ) )
c.close()

