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
        self.num = top
        self.dom = bottom

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

        commen_dividor = GCD(new_bottom, new_top)

        return Fraction(new_top // commen_dividor, new_bottom // commen_dividor)
    def __eq__(self, other):
        my_top = self.num * other.dom
        other_top = self.dom * other.num
        return my_top==other_top


## 以下是selfcheck的习题
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
##  x<y called x.__lt__(y)
    def __lt__(self,other):
        return self.num * other.dom > self.dom * other.num

##  x>y calls x.__gt__(y)
    def __gt__(self,other):
        return self.num * other.dom < self.dom * other.num

# test
my_fraction = Fraction(2,3)
other = Fraction(5,6)
print my_fraction > other
print my_fraction < other