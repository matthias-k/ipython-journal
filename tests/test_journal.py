import matplotlib
matplotlib.use('Agg')

from unittest import TestCase
import os
import glob
import shutil
import subprocess as sp

import matplotlib.pyplot as plt

import ipythonjournal

notebook = """
{
 "metadata": {
  "name": "Journal"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}
"""

class JournalTest(TestCase):
    def setUp(self):
        os.makedirs('tmp_dir')

    def assert_files_present(self, **kwargs):
        for ext in kwargs:
            files = glob.glob(os.path.join('Journal_files', '*.{0}'.format(ext)))
            self.assertEqual(len(files), kwargs[ext])
        if kwargs:
            total_count = sum(kwargs.values())
        else:
            total_count = 0
        all_files = glob.glob(os.path.join('Journal_files', '*'))
        self.assertEqual(len(all_files), total_count)


    def tearDown(self):
        if os.path.exists('Journal_files'):
            shutil.rmtree('Journal_files')
        if os.path.exists('tmp_dir'):
            shutil.rmtree('tmp_dir')

    def test_savefig(self):
        plt.plot([0, 1, 0])
        ipythonjournal.savefig()
        self.assert_files_present(png=1)

    def test_nbconvert(self):
        notebook_file = os.path.join('tmp_dir', 'notebook.ipynb')
        open(notebook_file, 'w').write(notebook)
        sp.check_call(['ipython-journal', notebook_file])
        self.assert_files_present(html=1)

    def test_import_file(self):
        import_file = os.path.join('tmp_dir', 'test.txt')
        open(import_file, 'w').write('test')
        ipythonjournal.get_journal().import_file(import_file)
        self.assert_files_present(txt=1)
