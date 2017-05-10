from valid import Domain

class Protein(Domain):
	def __init__(self, name):
		Domain.__init__(self, name)

	def foreach(self, sink, dimensions=''):
		Domain.foreach(
			self,
			lambda data: sink(data),
			'e.dimension>=0' if len(dimensions)==0 else 'e.dimension in ({})'.format(dimensions)
		)
