from __future__ import print_function
import random
import hashlib
import datetime
import sys
import os
import subprocess as sp
import shutil
import random

from pkg_resources import resource_string

def getId():
    return "%s-%s" % (datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:8])


class Journal(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def ensure_path_exists(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_filename(self, ext=None):
        filename = getId()
        if ext is not None:
            if not ext.startswith('.'):
                ext = ".{0}".format(ext)
            filename = "{0}{1}".format(filename, ext)
        filename = os.path.join(self.path, filename)
        return filename

    def savefig(self, figure=None):
        import matplotlib.pyplot as plt
        filename = self.get_filename(ext='.png')
        self.ensure_path_exists()
        if figure is None:
            figure = plt
        figure.savefig(filename, bbox_inches='tight')
        print('<img src="{0}" />'.format(filename))

    def save_dataframe(self, df):
        filename = self.get_filename(ext='.csv')
        self.ensure_path_exists()
        df.to_csv(filename)
        print("import pandas as pd; from IPython.display import HTML; df = pd.read_csv('{0}',index_col=0);HTML(df.to_html());#plt.figsize(20,5);df.T.plot(kind='bar')".format(filename))

    def save_notebook(self, notebook, template='toggle_no_input.tpl'):
        """
        Convert a notebook into an HTML file with inlined figures
        that is saved in the Journal's files directory.

        This will apply a template that by default hides the input
        cells. The idea is to have e.g. the full evaluation of
        some experiment in a notebook. If you want to save the
        results of this evaluation, this function will create
        a clean html file that by default shows all outputs.
        """

        # Unfortunately, ipython notebook does not support
        # templates outside current directory at the moment
        # Therefore we copy the template into the current
        # directory and delete it afterwards
        #file_location = os.path.realpath(__file__)
        #file_directory = os.path.dirname(file_location)
        #template_file = os.path.join(file_directory, 'data', template)

        local_template = None

        while not local_template or os.path.exists(local_template):
            local_template = template+str(random.randint(0, 1000))

        #if not os.path.exists(template_file):
        #    raise ValueError('Template file not found at', template_file)
        #shutil.copy(template_file, local_template)
        with open(local_template, 'wb') as f:
            f.write(resource_string(__name__, 'data/{}'.format(template)))
        self.ensure_path_exists()

        try:
            output_filename = self.get_filename()
            sp.check_call(['ipython', 'nbconvert', '--template', local_template, '--output', output_filename, notebook])

        finally:
            os.remove(local_template)

        print("[Linkname]({0}.html)".format(output_filename))


def get_journal():
    return Journal('Journal', 'Journal_files')


def savefig(figure=None):
    get_journal().savefig(figure=figure)


def save_dataframe(df):
    get_journal().save_dataframe(df)


def main():
    journal = get_journal()
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            ext = os.path.splitext(filename)[1]
            if ext.lower() == '.ipynb':
                journal.save_notebook(filename)
            else:
                raise NotImplementedError('cannot handle files of format {0}'.format(ext))

if __name__ == '__main__':
    main()
