from repository import Repository

repo = Repository()

for s in ['a','b','c']:
	repo.add(s)

repo.foreach(
	lambda a,b: print(a,b)
)
