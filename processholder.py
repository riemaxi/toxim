import os
import time

class ProcessHolder:
	user = ''
	proc_name = ''
	squeue_file = ''
	def __init__(self, user, proc_name):
		self.user = user
		self.proc_name = proc_name
		self.squeue_file = 'jobs.squeue'

	def hold(self):
		locked = True
		while locked:
			os.system('squeue -u {} -n {} > {}'.format(self.user, self.proc_name, self.squeue_file))	
			jobs = open(self.squeue_file).read().strip('\n').split('\n')
			print('# jobs: ', len(jobs) - 1)

			locked = len(jobs) > 1
			
			time.sleep(1)

	def prepare(self,content, dir):
		with open('{}/{}'.format(dir, self.proc_name),'w') as file:
			file.write(content) 
