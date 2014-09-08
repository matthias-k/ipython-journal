ipython-journal
===============


ipython-journal is a small library that helps in using an IPython notebook as lab journal. It makes it easy
to save plots and data from python or an IPython notebook in some directory and use it from the journal
notebook. It automatically assigns filenames based on the timestamp in order to make overwriting the data
impossible. Also it prints the code needed to show the plots or the data in an IPython notebook.

Example
=======


    >>> import ipythonjournal as journal
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

    >>> plt.plot(np.random.randn(10))
    >>> journal.savefig()

        <img src="files/Journal_files/2013-07-31_19-30-01-0ade76d1.png" />
    
Saving pandas dataframes is possible as well

    >>> import pandas as pd
    >>> df = pd.DataFrame(np.random.randn(4,3))
    >>> journal.save_dataframe(df)

        import pandas as pd; from IPython.display import HTML; df = pd.read_csv('Journal_files/2013-07-31_19-31-06-4978a3d1.csv',index_col=0);HTML(df.to_html());

By using the `Journal` class, you can specify where the files should be put. Later, some configuration options via
files might be added.

Saving full notebooks
=====================

Sometimes one would like to save a full notebook with evaluation results. ipython-journal provides
a command line interface that can convert a notebook into a HTML file that is saved within the
files directory of the journal. Also, a special template is applied that will by default hide all
code cells and show only output, as one is usually interested in saving the evaluation results.

Saving a notebook is quite easy:

    % ipython-journal somenotebook.ipynb
        ...
    [NbConvertApp] Writing 2653912 bytes to Journal_files/2014-09-08_18-07-05-737cf754.html
    [Linkname](Journal_files/2014-09-08_18-07-05-737cf754.html)

The last line shows that with `[Linkname](Journal_files/2014-09-08_18-07-05-737cf754.html)` we can
link this file from a markdown cell in some other notebook (e.g. the Journal notebook).

