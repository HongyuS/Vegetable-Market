class Flower:
    
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price
    
    def setName(self):
        self.name = input('Please enter the name of the flower:\n> ')
    
    def setPetals(self):
        while True:
            value = input('Please enter the number of petals:\n> ')
            try:
                self.petals = int(value)
                if self.petals < 0:
                    print('Number of petals cannot be negative!')
                    raise ValueError()
            except ValueError:
                print('Invalid input ...\nPlease try again!')
            else:
                break
    
    def setPrice(self):
        while True:
            value = input('Please enter the price of the flower:\n> ')
            try:
                self.price = float(eval(value))
                if self.price < 0:
                    print('The price cannot be negative!')
                    raise ValueError()
            except ValueError:
                print('Invalid input ...\nPlease try again!')
            else:
                break
    
    def show(self):
        print('The name of the flower is', self.name)
        print('The number of petals is', self.petals)
        print('The price of the flower is', self.price)

f = Flower('flower', 0, 0.0)
f.setName()
f.setPetals()
f.setPrice()
f.show()

