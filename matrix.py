from valid import Domain

class Matrix(Domain):
	COMPOUND_DIM = 0
	PROTEIN_DIM = 1
	SCORE_DIM = 2

	def __init__(self, name):
		Domain.__init__(self,name)

	def addScore(self, id, cid, pid, score = ''):
		if len(score)>0:
			self.addEntity(
				id,
				[(self.COMPOUND_DIM,cid),(self.PROTEIN_DIM,pid),(self.SCORE_DIM,score)]
			)
		else:
			self.addEntity(
				id,
				[(self.COMPOUND_DIM,cid),(self.PROTEIN_DIM,pid)]
			)
