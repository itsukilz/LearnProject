#coding=utf-8

# 以下是重写了一遍书上的示例
def GCD(m,n):
    while  m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n

    return n

class Fraction:
    def __init__(self,top,bottom):
        #1.7.5
        if int(top) == top and int (bottom) == bottom:
            commen_dividor = GCD(top, bottom)

            self.num = top//commen_dividor
            self.dom = bottom//commen_dividor
        else:

            raise ValueError('Two values must both be integer')


    def __str__(self):
        if self.dom == 0:
            raise ValueError ('Your dom can not be 0')
        else:
            if self.num == 0:
                return str(0)
            else :
                return str(self.num)+' / '+str(self.dom)

    def __add__(self,other):
        new_top = self.num * other.dom + self.dom * other.num
        new_bottom = self.dom * other.dom

        commen_dividor = GCD(new_top, new_bottom)

        return Fraction(new_top // commen_dividor, new_bottom // commen_dividor)
    def __eq__(self, other):
        my_top = self.num * other.dom
        other_top = self.dom * other.num
        return my_top==other_top


## 以下是1.7 exercises
    # 1.7.1
    def get_num(self):
        return self.num

    def get_den(self):
        return self.dom


## __mul__是*
    def __mul__(self,other):
        new_top = self.num * other.num
        new_bottom = self.dom * other.dom

        commen_dividor = GCD(new_top,new_bottom)
        return Fraction(new_top//commen_dividor, new_bottom//commen_dividor)
## __div__是/
    def __div__(self,other):
        new_top = self.num * other.dom
        new_bottom = self.dom * other.sum
        commen_dividor = GCD(new_top,new_bottom)
        return Fraction(new_top//commen_dividor, new_bottom//commen_dividor)
## __sub__是 - 
    def __sub__(self,other):

        new_top = self.num * other.dom - self.dom * other.num
        new_bottom = self.dom * other.dom        

        commen_dividor = GCD(abs(new_top),abs(new_bottom))
        return Fraction(new_top//commen_dividor, new_bottom//commen_dividor)
##  x<y __lt__
    def __lt__(self,other):
        return self.num * other.dom > self.dom * other.num

##  x>y __gt__
    def __gt__(self,other):
        return self.num * other.dom < self.dom * other.num
##  x >= y __ge__
    def __ge__(self,other):
        return self.num * other.dom >= self.dom * other.num
##  x<=y __le__
    def __le__(self,other):
        return self.num * other.dom <= self.dom * other.num
## x != y __ne__
    def __ne__(self,other):
        return self.num * other.dom != self.dom * other

## __radd__ 
    def __radd__(self,other):
        new_top = self.num * other.dom + self.dom * other.num
        new_bottom = self.dom * other.dom

        commen_dividor = GCD(new_bottom, new_top)
## __iadd__ x += y
    def __iadd__(self,other):
        self = self + other
        return self
## __repr__ 是用来
    def __repr__(self):
        return "Fraction(num = %d, dom = %d)" % (self.num, self.dom)
# test
my_fraction = Fraction(-2,3)
other = Fraction(7,3)


print repr(my_fraction)
