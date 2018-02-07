
import os

from IPython.display import display, HTML

from .params import Params
from .template import Template


class ImageTabs:
    """
    """

    def __init__(self,
                 data,
                 params,
                 verbose=False):

        self.params = Params(data=data,
                             **params,
                             verbose=verbose)

        self.template = Template(params=self.params)

        self.html = self.template.content

    def show(self):
        """
        display image tabs
        """
        display(HTML(self.html))
