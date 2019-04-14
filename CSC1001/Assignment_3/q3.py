import random

class EcoSystem:

    def __init__(self, length, bear, fish, n):
        self.length = length
        self.river = ['B']*bear + ['F']*fish + ['N']*(length-bear-fish)
        random.shuffle(self.river)
        self.n = n
    
    def addAnimal(self, animal):
        if self.river.count('N') > 0:
            choices = [i for i, x in enumerate(self.river) if x=='N']
            index = random.choice(choices)
            self.river[index] = animal

    def updateRiver(self):
        for i in range(len(self.river)):
            if self.river[i] != 'N':
                change = random.choice([-1, 1])
                if 0 <= i + change and i + change < self.length:
                    if self.river[i + change] == 'N':
                        self.river[i + change] = self.river[i]
                        self.river[i] = 'N'
                    elif self.river[i] == self.river[i+change]:
                        if self.river[i] == 'B':
                            self.addAnimal('B')
                        else:
                            self.addAnimal('F')
                    else:
                        if self.river[i] == 'B': 
                            self.river[i + change] = self.river[i]
                        self.river[i] = 'N'

    def printRiver(self):
        river = '|'
        for i in self.river:
            if i == 'B':
                river += '🐻'
            elif i == 'F':
                river += '🐟'
            elif i == 'N':
                river += '🌫'
        river += '|'
        print('\n' + river + '\n')
    
    def simulation(self):
        for i in range(self.n):
            self.printRiver()
            self.updateRiver()


def inputInt(parameter):
    while True:
        value = input('Please enter {}:\n> '.format(parameter))
        try:
            value = int(value)
            if value < 0:
                raise ValueError()
        except ValueError:
            print('Invalid input ...\nPlease try again!')
        else:
            break
    return value


if __name__ == "__main__":
    length = inputInt('the length of the river')
    while True:
        bear = inputInt('the number of bears')
        fish = inputInt('the number of fishes')
        if length-bear-fish >= 0:
            break
        else:
            print('Too many bears and fishes!\nPlease enter again.')
    n = inputInt('the number of steps you want to simulate')
    r = EcoSystem(length, bear, fish, n)
    r.simulation()
