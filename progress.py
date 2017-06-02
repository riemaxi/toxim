from valid import Domain

class Progress(Domain):
	INITIAL_STATE = 0
	GRID_PREPARED_STATE = 1
	GRID_CREATED_STATE = 2
	LIGAND_PREPARED_STATE = 3
	PARAMETER_CREATED_STATE = 4

	def __init__(self, name):
		Domain.__init__(self,name)

	def addState(self, cid, pidim, pid, state):
		self.pushEntity(cid, [(pidim, '{}:{}'.format(pid,state))])


	def foreach(self, sink, criteria = ''):
		Domain.foreach(
			self,
			lambda data: sink([value for id,value in data])
		)
