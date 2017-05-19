from valid import Domain

class Matrix(Domain):
	PROTEIN_DIM = 0
	SCORE_DIM = 1

	def __init__(self, name):
		Domain.__init__(self,name)

	def addScore(self, cid, pid, score = ''):
		if len(score)>0:
			self.addEntity(
				cid,
				[(self.PROTEIN_DIM,pid),(self.SCORE_DIM,score)]
			)
		else:
			self.addEntity(
				cid,
				[(self.PROTEIN_DIM,pid)]
			)
