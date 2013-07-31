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
