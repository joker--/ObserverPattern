""" This is the observable class which observers can register to"""

class Observable:
    """Observable Class"""

    def __init__(self):
        self.observers=[]

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
            print("Observer %s registered" % observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observer.remove(observer)
            print("Observer %s removed" % observer)

    def unregister_all(self):
        del self.observers[:]
        print("Unregistered all observers")

    def update_observers(self, * args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


