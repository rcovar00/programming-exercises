global_var = 1


def my_function(animal):
    print 'Locals: ', locals()
    print 'Globals: ', globals()


my_function('dog')
