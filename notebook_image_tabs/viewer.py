
import os
import datetime as dt

from IPython.display import display, HTML

from .params import Params
from .template import Template


class ImageTabs:
    """
    """

    def __init__(self,
                 data,
                 params,
                 iframe=True,
                 verbose=False):

        self.params = Params(data=data,
                             **params,
                             verbose=verbose)

        self.template = Template(params=self.params,
                                 iframe=iframe)

        self.html = self.template.content

    def show(self):
        """
        display image tabs
        """
        display(HTML(self.html))

    def save(self,
             folder='dump',
             name=None,
             tagged=True):
        """
        save as file
        """
        if not os.path.exists(folder):
            os.makedirs(folder)
        if not name:
            name = 'myplot'
        tag = ''
        if tagged:
            tag = dt.datetime.now().strftime('_%Y%m%d_%H%M%S')
        suffix = '.html'
        filename = '{}{}{}'.format(name, tag, suffix)
        path = os.path.join(folder, filename)

        with open(path, 'w') as f:
            f.write(self.html)
