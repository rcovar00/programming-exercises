class Shape(object):

    def __init__(self, name, value=2):
        self.name = name
        self.value = value

    def __len__(self):
        return 4

    def __del__(self):
        print "Deleted"

    def __str__(self):
        return "New shape"

    def __cmp__(self, other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        else:
            return 0


a = Shape('circle')
print a.name
print a
print len(a)

b = Shape(name='rectangle', value=1)
print b < a
