from parameter import Parameter
from compound import Compound

p = Parameter()

sep = '\t' if p._('compound_report.sep') == 'tab' else p._('compound_report.sep')

structure = p._('compound.fetch.structure')
c = Compound(p._('compound.db'))
c.listAll( lambda data: print('{1}{0}{2}{0}{3}/{4}.{5}'.format(sep, data[1], data[0], structure, data[1],'sdf') ) )
c.close()

