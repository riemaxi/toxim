import os

class ProcessHolder:
	def ___init___(self, user, proc_name, template):
		self.user = user
		self.proc_name = proc_name
		self.template = template

		self.squeue_file = 'jobs.squeue'

	def hold(self):
		locked = True
		while locked:
			os.system('squeue -u {} -n {} > {}'.format(self.user, self.proc_name, self.queue_file))	
			jobs = open(self.squeue_file).read().strip('\n').split('\n')
			print('# jobs: ', len(jobs) - 1)
			
			time.sleep(1)

	def prepare(self,content, dir):
		with open('{}/{}'.format(self.dir, self.proc_name),'w') as file:
			file.write(content) 
