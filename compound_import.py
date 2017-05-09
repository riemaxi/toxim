from compound import Compound
from parameter import Parameter

p = Parameter()

cmp = Compound(p._('compound.db'))
cmp.importData(p._('compound.import'),20)
cmp.close()
