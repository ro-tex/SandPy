import random
import time


def hi():
    """Prints out "Hello Python!"
    """
    print "Hello Python!"

### STRINGS ###


s = "this is a string"
print s[2:-5]  # substring. both parts are optional

# see https://www.tutorialspoint.com/python/python_strings.htm
# string formatting is a bit weird: "pattern" % (fillers)
print "This is a %s string. %d is an int, %f is a float." % ("formatted", 9, 3.14)
print "Hello World!"[:6] + "Python!"  # this is interesting

### LISTS ###

sep = "-"
strings = ["a", "b", "c"]
# joining is a bit... reversed - you cast it on the separator:
print sep.join(strings)
print ">>>", "  stripping whitespaces   ".strip(), "<<<"

arr = ['zero', 1, True, 3.14, "four"]  # a list
arr.append(5)
arr.extend([9, 8, 7])  # append the elements of an iterable
print arr[1:]  # list slicing - just like go

print [1, 2, 3] + [4, 5, 6]  # -> [1, 2, 3, 4, 5, 6] arr concat? :)

# slice and dice lists
list = ['php', 'java', 'ruby'][1:] + ['go', 'rust', 'python']
del list[3]
# list.append('c') # adds one element
# list.extend(tup) # adds a whole list of elements
# list.pop(); list.remove('c'); etc... no shift/unshift, though - use list.insert()
print list

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
    # this will be skipped if we break out of the loop
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
random.shuffle(arr)  # shuffles the structure, returning none
print random.choice(arr)  # random element of arr
print random.random(), random.uniform(5, 10)  # rand 0..1, rand 5..10
