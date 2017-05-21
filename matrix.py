from valid import Domain

class Matrix(Domain):
	PROTEIN_DIM = 0
	SCORE_DIM = 1
	IS_3D_DIM = 2

	def __init__(self, name):
		Domain.__init__(self,name)

	def addCompound(self, cid, is3d = True):
		self.addEntity(cid, [(self.IS_3D_DIM,is3d)])

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
