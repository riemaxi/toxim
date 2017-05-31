
data = open('data.txt').read().strip('\n').split('\n')

if len(data):
	with open('data.txt','w') as file:
		file.write('\n'.join(data[1:]))


