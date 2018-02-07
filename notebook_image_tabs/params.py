
import json
import random

from copy import deepcopy as copy

from .util import load_img


class Params:
    """
    """

    def __init__(self,
                 data=None,
                 verbose=False,
                 **kwargs):
        """
        Set params incl. defaults
        """
        # attributes
        self.uuid = random.randint(0, int(1e9))

        self.data = data
        self.borderPx = 0
        self.borderColor = 'white'
        self.tabBackgroundColor = 'white'
        self.buttonMargin = 5
        self.buttonPaddingVert = 10
        self.buttonPaddingHori = 8
        self.buttonBorderColor = 'white'
        self.imageWidthPerCent = 99

        self.selection = 0

        self.buttonColorBase = '#eeeeee'
        self.buttonColorHover = '#dddddd'
        self.buttonColorActive = '#bdbdbd'

        for k, v in kwargs.items():
            setattr(self, k, v)
        self.valid = self.check(verbose=verbose)

        self.data = self.build_data()


    def check(self, verbose=False):
        """
        """
        msg = 'data must be a list'
        assert isinstance(self.data, list), msg
        for e in self.data:
            msg = 'each element of data must be a list'
            assert isinstance(e, list), msg
            msg = 'each elemnt of data must have length 2'
            assert len(e) == 2, msg
            name, value = e
            msg = 'data element name must be a string'
            assert isinstance(name, str), msg
            msg = 'data element value must be bytes'
            assert isinstance(name, (str, bytes)), msg

        if verbose:
            print('data is valid')

        return True

    def build_data(self):
        """
        """
        data2 = []
        for e in self.data:
            name, str_img = e
            str_b64 = load_img(str_img)
            data2.append([name, str_b64])
        return data2

    def to_dict(self):
        """
        """
        d = copy(self.__dict__)
        d = {k: v for k, v in d.items() if v is not None}
        return d

    def pprint(self, indent=2):
        """
        """
        d = json.dumps(self.to_dict(),
                       sort_keys=True,
                       indent=indent)
        print(d)

    def __repr__(self):
        return str(self.to_dict())
