import os
import random
import time
from time import gmtime  # import just one method, use it without module prefix

from rolib import *  # don't go wild with this one - pollutes the namespace


def hi():
    '''Prints out "Hello Python!"'''
    print "Hello Python!"

### STRINGS ###


s = "this is a string"
print s[2:-5]  # substring. both parts are optional

# see https://www.tutorialspoint.com/python/python_strings.htm
# string formatting is a bit weird: "pattern" % (fillers)
print "This is a %s string. %d is an int, %f is a float." % ("formatted", 9, 3.14)
print "Hello World!"[:6] + "Python!"  # this is interesting

### LISTS ###

strings = ["a", "b", "c"]
# joining is a bit... reversed - you cast it on the separator:
# and you can't pass a list of ints instead of strings
print ' - '.join(strings)
print ">>>", "  stripping whitespaces   ".strip(), "<<<"

# string methods do NOT change the original string (strip, capitalize, etc...)

arr = ['zero', 1, True, 3.14, "four"]  # a list
arr.append(5)
arr.extend([9, 8, 7])  # append the elements of an iterable
print arr[1:]  # list slicing - just like go

print [1, 2, 3] + [4, 5, 6]  # -> [1, 2, 3, 4, 5, 6] arr concat? :)

# results in a new list where every element of arr is *2-ed:
arr2 = [elem * 2 for elem in arr]
# the same concept with nested fors:
pairs = [(x, y) for x in arr for y in arr2]

# slice and dice lists
list = ['php', 'java', 'ruby'][1:] + ['go', 'rust', 'python']
del list[3]
# list.append('c') # adds one element
# list.extend(tup) # adds a whole list of elements
# list.pop(); (no push) list.remove('c'); etc... no shift/unshift, though - use list.insert()
print list  # ['java', 'ruby', 'go', 'python']

### TUPLES ###

# tuples are immutable
tup = ('zero', 1, True, 3.14, "four")  # yup, this is a tuple. with 5 values
print tup[1:-1]  # we can slice them just like lists
tup2 = 'foo', 'bar', 2  # the parntheses are optional
empty, single = (), (50,)   # except when empty or single - notice the trailing comma!
# del tup2[2] -> throws an error, tuples are immutable
del tup2  # this is fine - we're removing the whole thing

s, fs = set(tup * 2), frozenset(tup * 2)
print s, fs

### DICTS ###

dic = {1: "one", "two": 2}  # mixing types in keys and values
print dic, dic["two"], dic.keys(), dic.values()
dic['foo'] = 'bar'
del dic['foo']
dic.clear()  # wipe the whole thing
dic.get('foo', None)  # get the value for 'foo' or None if 'foo' is not there
# set 'foo' to None only if it's not already in the dict:
dic.setdefault('foo', None)
dic.items()  # returns a series of (key,value) tuples
# join another dict into the original, overwriting duplicate keys:
dic.update({'foo': 'bar', 'lala': 'blabla'})

# Char ops: chr(61), ord('a'), unichr(61)

# Binary operations:
#   a, b = 0b00111100, 0b00001101
#  a & b = 0b00001100 AND
#  a | b = 0b00111101 OR
#  a ^ b = 0b00110001 XOR
#     ~a = 0b11000011 NOT
# a << 2 = 0b11110000 left/right shift

# Logical ops: and, or, not

# Membership ops: in, not in

# Memory identity ops: is, is not - whether two variables point to the same memory

# No tertiary if (?:); no case/switch; elif:
n = 5
if n < 0:
    print "negative"
elif n > 0:
    print "positive"
else:
    print "zero"

while n == 5:
    print "In a while loop..."
    n -= 1  # yeah, no n++/n-- :(
else:
    # this will be skipped if we break out of the loop (or throw an exception)
    print "...and we exited the while without a break!"

# Ye olde foreach:
for el in arr:
    print ">>", el, "<<"
    break
else:
    print "we can 'else' here, too"

for i in range(2, len(arr)):  # we can play around with this range a lot. Almost like Ruby <3
    print ">>", arr[i], "<<"
    break

random.seed(time.clock())  # seed with current CPU time (a float)
random.shuffle(arr)  # shuffles the structure, returning None
print random.choice(arr)  # random element of arr
print random.random(), random.uniform(5, 10)  # rand 0..1, rand 5..10

t = time.time()
print 'UNIX time:', t, '\tReadable time:', time.ctime(), '\tLocal readable time:', time.asctime(time.localtime(t))

### FUNCTIONS ###


def foo(a=0, b=1, c=2):
    '''Prints the input vars. Has default values (we can skip args).'''
    print 'foo:', "A: %d, B: %d, C: %d" % (a, b, c)


foo()  # prints out the defult values
# args in random order but named:
foo(c=3, a=1, b=2)  # these are not defined as veriables a, b and c outside!


def bar(*args):
    ''' Works on any number of arguments, all caught in the args variable.
        The function can have other args as well but while we can pass those as
        named paramters, we cannot pass the *args in a named form - the *args tuple
        will catch anything that's beyond the required params.
    '''
    # for x in args: print x
    print 'bar:', " - ".join(args)


b = bar  # functions are first class citizens! we can pass them as values! :)
b('a', 'b', 'c')

### LAMBDAS ###

''' Lambdas in Python aren't really "anonymous functions" but rather just named expressions.
    They are similar to Ruby's lambdas and very different from Go's anon funcs.
    They don't have access to variables which haven't been passed as arguments (local namespace).
'''

# defining two, so the linter won't convert them to regular functions:
l1, l2 = lambda x, y: x**y, lambda x, y: x + y
print 'Lambdas:', l1(3, 5), l2(3, 5)

print hello()  # calling a method from a module

# yes, you can do this - raw strings just hanging around like that:
"let's play with variable scoping for a bit:"
glob = 1  # a global var


def func_gen():
    glob = 2  # this will never be used - it's local but not to inner()

    def inner():
        'This function is a closure.'
        # glob = 3  # if we do those, glob will always be a local var, even if we call `global glob`
        global glob  # skips the glob = 2 and uses glob = 1. otherwise uses glob = 2
        return glob
    return inner


f = func_gen()
print f()

### I/O ###

# s = raw_input('Enter something:') # we get raw string into s
# evaluates the input as Python code and stores the result into s:
# s = input('Enter someting (it can be Python code):')

my_file = open('file.dat', 'w+')  # check access_modes - there's binary rw
my_file.write('loren ipsum\n')
my_file.close()  # we need to do that. also flushes the buffers

my_file = open('file.dat', 'r')
# we set a limit on the read, otherwise it will read the entire file into memory (or at least attempt to):
content = my_file.read(200)  # reads only what is there, doesn't pad to 200
my_file.tell()  # at which position in the file are we?
# go to position 0, so we can read/write from there. the second param is a reference point -
# should we move to 0 from the start of the file (0), the current position (1) or the end of the file (2):
my_file.seek(0, 0)
my_file.close()
print '>>>', content, '<<<'

os.rename('file.dat', 'del_me.dat')
os.remove('del_me.dat')  # delete the file

### EXCEPTIONS ###

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
    raise AssertionError, 'Error message'

except (IOError, AssertionError), ex:  # we can catch multiple like this

    # import pdb; pdb.set_trace()  # this is how we set a breakpoint!
    print "Error: can\'t find file or read data.", ex

except ex:  # considered bad style
    print "Error: something else happened!", ex

else:  # no exception was raised
    print "Written content in the file successfully"
    fh.close()

finally:
    print 'finally'


def args(arg, *args, **kwargs):
    # The *args and **kwargs names are the established naming convention
    print arg       # a single arg
    print args      # an array of args
    print kwargs    # a dict of named args


args('a', 'b', 'c', foo=3, bar=4)

# get [1..100], filter the numbers below 5, square each of them and sum the resulting list:
print 'Get the squares of [1, 2, 3, 4] and sum them with filter-map-reduce:', \
    reduce((lambda x, y: x + y), map((lambda x: x**2),
                                     filter((lambda x: x < 5), range(100))))

funcs = [
    lambda x: x * 2,  # we can use function names here, too
    lambda x: x * 3,
    lambda x: x * x
]

# a map operating on multiple input iterables:
print 'Run a set of funcs on [1, 2, 3]:', map((lambda x, y: x(y)), funcs, [1, 2, 3])
