class Instrument:

    def __init__(self, price):
        self.price = price

    def play(self):
        pass

    def sell(self):
        print "You're selling the instrument"


class Guitar(Instrument):

    def play(self):
        print "You're playing guitar"


class Violin(Instrument):

    def play(self):
        print "You're playing violin"


guitar = Guitar(23)
print guitar.price
guitar.play()
