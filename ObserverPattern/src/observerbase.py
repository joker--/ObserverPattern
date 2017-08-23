""" Observer abstract base class"""

from abc import ABCMeta, abstractmethod

class BaseClass(metaclass=ABCMeta):
    '''Base class for creating observers'''

    def update(self, *args, **kwargs):
        pass # no need to define here. will handle in derived

