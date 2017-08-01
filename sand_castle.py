from structure import Structure


class SandCastle (Structure):  # inheritance
    '''Defines a sand castle.'''

    __num_castles = 0   # private class field
    purpose = 'fun'     # public class field

    # Constructor:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        SandCastle.__num_castles += 1

    # Destructor:
    def __del__(self):
        class_name = self.__class__.__name__
        SandCastle.__num_castles -= 1
        print class_name, self.name, "destroyed"

    # Serialize this object to evaluatable code:
    def __repr__(self):
        return

    # Serialize this object to printable string:
    def __str__(self):
        return "Castle. Name: %s, size: %s." % (self.name, str(self.size))

    # Custom comparator:
    def __cmp__(self, other):
        if self.size < other.size:
            return -1
        elif self.size > other.size:
            return 1
        else:
            return 0

    # Overload the '+' operator for sand castles:
    def __add__(self, other):
        # also __sub__, __mul__, __div__, etc.
        # for a list see https://docs.python.org/2/library/operator.html
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

print 'age:', getattr(c, 'age', 0)  # default to 0 if 'age' does not exist
setattr(c, 'age', 2)
print 'has attribute?', hasattr(c, 'age')
delattr(c, 'age')  # another way to delete an attribute

print 'Is subclass?', issubclass(SandCastle, Structure)
print 'Is instance?', isinstance(c, SandCastle)

del c  # destroy the object
