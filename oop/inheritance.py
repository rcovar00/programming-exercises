class Instrument:
    id = 1

    def __init__(self, price):
        self.price = price
        self.size = 'small'

    def play(self):
        print "We are playing"


class Guitar(Instrument):
    pass


class Violin(Instrument):
    pass


guitar = Guitar(2500)
print guitar.price
guitar.play()

violin = Violin(3000)
violin.size = 'big'

print getattr(guitar, 'size')
print getattr(violin, 'size')
print hasattr(guitar, 'dimensions')
