class Derivative:
    
    def inputPol(self):
        self.polynomial = input('Please enter a polynomial with one unkown:\n> ')
        self.polynomial = self.polynomial.replace('-', '+-')
    
    def setTerms(self):
        self.terms = self.polynomial.split('+')
        for i in range(len(self.terms)):
            try:
                int(self.terms[i])
            except:
                continue
            else:
                self.terms.remove(self.terms[i])
    
    def setCoe(self):
        self.coe = list()
        for i in self.terms:
            try:
                self.coe.append(int(i.split('*')[0]))
            except:
                self.coe.append(1)

    def setPower(self):
        self.power = list()
        for i in self.terms:
            try:
                self.power.append(int(i.split('^')[1]))
            except:
                self.power.append(1)
    
    def derivative(self):
        self.poly_der = ''
        self.x = self.terms[0].split('*')[1].split('^')[0]
        for i in range(len(self.terms)):
            self.coe[i] = self.coe[i] * self.power[i]
            self.power[i] -= 1
            if self.power[i] == 0:
                self.terms[i] = str(self.coe[i])
            else:
                if self.coe[i] > 1:
                    self.terms[i] = str(self.coe[i]) + '*' + self.x
                elif self.coe[i] == 1:
                    self.terms[i] = self.x
                if self.power[i] > 1:
                    self.terms[i] += ('^'+str(self.power[i]))
            if self.terms[i][0] != '-' and i > 0:
                self.terms[i] = '+' + self.terms[i]
            self.poly_der += self.terms[i]
        print('\nThe first derivative with respect to {} is:\n{}'.format(self.x, self.poly_der))
    
    def take_derivative(self):
        self.inputPol()
        self.setTerms()
        self.setCoe()
        self.setPower()
        self.derivative()


if __name__ == '__main__':
    Derivative().take_derivative()

# e.g.: 2*x^3+3*x^2-5*x+1
