import sys
from valid import Domain

class Compound(Domain):

	def __init__(self,name):
		Domain.__init__(self, name)

	def listAll(self, sink):
		Domain.foreach(
			self, 
			lambda data: sink( (data[-1][1],data[0][1],data[1][1]) ),
			'e.dimension in (1,3)'
			)
