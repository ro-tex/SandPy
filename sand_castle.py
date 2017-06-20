from structure import Structure


class SandCastle (Structure):  # inheritance
    'Defines a sand castle.'

    __num_castles = 0  # private class field
    purpose = 'fun'  # public class field

    # Constructor:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        SandCastle.__num_castles += 1

    # Destructor:
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, self.name, "destroyed"

    def __repr__(self):
        # How to serialize this object to evaluatable code
        return

    def __str__(self):
        # How to serialize this object to printable string
        return

    def __cmp__(self, other):
        # Custom comparator
        if self.size < other.size:
            return -1
        elif self.size > other.size:
            return 1
        else:
            return 0

    def __add__(self, other):
        # Overloading the '+' operator for sand castles
        return

    # Override the parent method:
    def get_greeting(self):
        return "Welcome to castle %s!\nWe have %d more castles!" % (self.name, SandCastle.__num_castles - 1)

    @staticmethod  # we need a decorator in order to make a static method
    def static():
        return "I am a static method."


c = SandCastle('SandyBurg', 'small')
print c.get_greeting()

print SandCastle.static()

del c.size  # WE CAN DELETE ATTRIBUTES! WTF!??!?!
getattr(c, 'age', 1)
setattr(c, 'age', 2)
hasattr(c, 'age')
delattr(c, 'age')

print 'Is subclass?', issubclass(SandCastle, Structure)
print 'Is instance?', isinstance(c, SandCastle)

del c  # destroy the object
