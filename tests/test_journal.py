from unittest import TestCase
import os
import shutil
import matplotlib.pyplot as plt

import ipythonjournal

class JournalTest(TestCase):
    #def tearDown(self):
    #    if os.path.exists('Journal_files'):
    #        shutil.rmtree('Journal_files')
    def test_a(self):
        plt.plot([0,1,0])
        ipythonjournal.savefig()
