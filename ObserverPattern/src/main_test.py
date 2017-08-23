""" Unit test Observer Pattern"""
import unittest
from Observable import Observable
from observerbase import BaseClass


class TestObserver(BaseClass):
    def __init__(self):
        args = []
        kwargs = {}

    def update(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return


class UnitTestObserver(unittest.TestCase):
    '''Testing class'''

    def setUp(self):
        self.undOb = Observable()
        self.bot1 = TestObserver()
        self.bot2 = TestObserver()

    def tearDown(self):
        del self.undOb
        del self.bot1
        del self.bot2

    def test_defaultNoObserver(self):
        self.assertEqual(len(self.undOb.observers),0," Observer list is not empty")

    def test_DuplicateObservers(self):
        self.undOb.register(self.bot1)
        self.undOb.register(self.bot2)
        self.undOb.register(self.bot1)
        self.assertEqual(len(self.undOb.observers),2,"Duplicate observers registered")

    def test_RemoveAllSubscribers(self):
        self.undOb.register(self.bot1)
        self.undOb.register(self.bot2)
        self.undOb.register(self.bot1)
        self.undOb.unregister_all()
        self.assertEqual(len(self.undOb.observers), 0, "Observers still registered")


if __name__ == "__main__":
    unittest.main()



