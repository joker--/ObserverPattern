""" Main app to test observer pattern"""
from Observable import Observable
from observerbase import BaseClass

class ObserverA(BaseClass):
    '''A type of observerA class'''

    def __init__(self):
        '''Observer A constructor'''

    def update(self, *args, **kwargs):
        '''update callback which would be invoked'''
        print("ObserverA update invoked")
        for arg in args:
            print(arg)
        for key,value in kwargs.items():
            print(key,":",value)

class ObserverB(BaseClass):
    '''A type of observerA class'''

    def __init__(self):
        '''Observer A constructor'''

    def update(self, *args, **kwargs):
        '''update callback which would be invoked'''
        print("ObserverB update invoked")
        for arg in args:
            print(arg)
        for key,value in kwargs.items():
            print(key,":",value)


if __name__ == "__main__":
    underObservation = Observable()

    bot1 = ObserverA()
    bot2 = ObserverB()

    underObservation.register(bot1)
    underObservation.register(bot2)

    underObservation.update_observers(('SMA indicates SELL', 'Bollinger Resistance', 'SELL'), {"Lotsize": 37,
                                                                                               "TakeProfit": 300,
                                                                                               "SL": 50})

