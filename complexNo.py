import math

class ComplexNo:
 
    def complexNotation(self):                          # Converts the complex number into a+ib form
        self.ans=f"{self.real}+{self.imag}i" 
        if "+0i" in self.ans:                          
            self.ans=f"{self.real}"
        elif "+1i" in self.ans or "+1.0i" in self.ans:
            self.ans=f"{self.real}+i"
        elif "-1i" in self.ans or "-1.0i" in self.ans:
            self.ans=f"{self.real}-i"
        elif "+-" in self.ans:
            self.ans=f"{self.real}{self.imag}i"
        return self.ans

    def __init__(self,real,imag):                       # Constructor to construct a complex number
        self.real=real                                 
        self.imag=imag
        self.complexNotation()
    
    def __add__(self,other):                            # Adds two complex numbers c1 and c2. Syntax:   c1+c2
        real=self.real+other.real
        imag=self.imag+other.imag
        newComplex=ComplexNo(real,imag)                 
        return newComplex

    def __sub__(self,other):                            # Subtract a complex number c2 from c1. Syntax:    c1-c2
        real=self.real-other.real
        imag=self.imag-other.imag
        newComplex=ComplexNo(real,imag)
        return newComplex

    def __mul__(self,other):                            # Multiply two complex numbers c1 and c2. Syntax:   c1*c2
        real=(self.real*other.real)-(self.imag*other.imag)
        imag=(self.imag*other.real) + (self.real*other.imag)
        newComplex=ComplexNo(real,imag)
        return newComplex

    def __truediv__(self,other):                        # float division between two complex numebers c1 and c2. Syntax:    c1/c2
        real=(self*other.conj()).real/(other.real**2+other.imag**2)
        imag=(self*other.conj()).imag/(other.real**2+other.imag**2)
        newComplex=ComplexNo(real,imag)
        return newComplex

    def __floordiv__(self,other):                       # floor division between two complex numebers c1 and c2. Syntax:    c1//c2
        real=((self*other.conj()).real)//(other.real**2+other.imag**2)
        imag=((self*other.conj()).imag)//(other.real**2+other.imag**2)
        newComplex=ComplexNo(real,imag)
        return newComplex

    def __str__(self):                                  # Printing a complex number c1. Syntax:    print(c1)
        return self.ans

    def arg(self):                                      # Returns the argument of a complex number c1. Syntax:   c1.arg()
        return math.atan(self.real/self.imag)

    def __pow__(self,n):                                # Returns the exponential of a complex number c1 to the power n. Syntax:   c1**n
        s,pos_s,neg_s=0,0,0
        def ipow(power):
            if power%4==0:
                return 1
            elif (power+2)%4==0:
                 return -1

        for r in range(0,n+1):
            if (n-r)%2==0:
                s=s+ ((math.factorial(n))//(math.factorial(r)*math.factorial(n-r)))*(self.real**r)*((self.imag**(n-r))*ipow(n-r))
            elif (n-r+1)%4==0:
                neg_s=neg_s+ ((math.factorial(n))//(math.factorial(r)*math.factorial(n-r)))*(self.real**r)*(self.imag**(n-r))
            elif (n-r+3)%4==0:
                pos_s=pos_s + ((math.factorial(n))//(math.factorial(r)*math.factorial(n-r)))*(self.real**r)*(self.imag**(n-r))
        real=s
        imag=pos_s-neg_s
        newComplex=ComplexNo(real,imag)
        return newComplex
    
    def mod(self):                                      # Returns the modulus of a complex number c1. Syntax:   c1.mod()                                                                               
        return math.sqrt(self.real**2 + self.imag**2)

    def conj(self):                                     # Returns the conjugate of a complex number c1. Syntax:   c1.conj() 
        newComplex=ComplexNo(self.real,-self.imag)
        return newComplex

    def sqrt(self):                                     # Returns the square root of a complex number c1. Syntax:   c1.sqrt() 
        real=math.sqrt((self.mod() + self.real)/2)
        if self.imag==0:
            imag=0
        else:
            imag=(self.imag//math.fabs(self.imag))*math.sqrt((self.mod()-self.real)/2)
        newComplex=ComplexNo(real,imag)
        return newComplex

