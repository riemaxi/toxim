from parameter import Parameter
from compound import Compound

p = Parameter()

structure = p._('compound.fetch.structure')
c = Compound(p._('compound.db'))
c.listAll( lambda data: print('{},{},{}/{}.{}'.format(data[1], data[0], structure, data[1],'sdf') ) )
c.close()

