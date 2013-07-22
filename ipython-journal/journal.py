import random
import hashlib

import matplotlib.pyplot as plt

def getId():
	return "%s-%s" % (datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), hashlib.sha1("%s" % random.random()).hexdigest()[:8])

class Journal(object):
	def __init__(self, name, path):
		self.name = name
		self.path = path
	def get_filename(self, ext=None):
		filename = getId()
		if ext is not None:
			if not ext.startswith('.'):
				ext = ".{0}".format(ext)
			filename = "{0}{1}".format(filename, ext)
		filename = os.path.join(self.path, filename)
		return filename
	def savefig(self):
		filename = self.get_filename(ext='.png')
		plt.savefig(filename)
		print '<img src="files/{0}" />'.format(os.path.split(filename)[-1])

def get_journal():
	return Journal('Journal', 'files')

def savefig():
	get_journal().savefig()