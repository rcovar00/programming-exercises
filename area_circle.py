def area(radius):
    global pi
    pi = 3.1415926
    print "The area of a circle with radius %f is %f " % (radius, pi * radius ** 2)


pi = "pi"
print "pi value:", pi

area(2)
print "pi value:", pi
