from compound import Compound
from parameter import Parameter

p = Parameter()

d = Compound(p._('compound.db'))

d.xforeach(
	'select * from value',
	lambda data: print(data)
)

d.close()

