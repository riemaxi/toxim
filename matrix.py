from valid import Domain

class Matrix(Domain):
	SCORE_DIM = 0

	def __init__(self, name):
		Domain.__init__(self,name)

	def addScore(self, cid, dim, score):
		self.pushEntity(cid,[(dim, score)])
