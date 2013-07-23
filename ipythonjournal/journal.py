import random
import hashlib
import datetime
import os

import matplotlib.pyplot as plt
import pandas as pd

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
		print '<img src="files/{0}" />'.format(filename)
	def save_dataframe(self, df):
		filename = self.get_filename(ext='.csv')
		df.to_csv(filename)
		print "import pandas as pd; from IPython.display import HTML; df = pd.read_csv('{0}',index_col=0);HTML(df.to_html());#plt.figsize(20,5);df.T.plot(kind='bar')".format(filename)

def get_journal():
	return Journal('Journal', 'Journal_files')

def savefig():
	get_journal().savefig()