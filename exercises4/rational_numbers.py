from __future__ import division
import math
class Rational(object):
    def __init__(self, numer, denom):
        gcd = math.gcd(numer, denom)
        self.numer = int(numer / gcd)
        self.denom = int(denom / gcd)
        if numer < 0 or denom < 0:
            self.numer = -1 * abs(self.numer)
            self.denom = abs(self.denom)
            
    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom
    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)
    def __add__(self, other):
        return Rational(self.numer*other.denom + self.denom*other.numer,
                        self.denom * other.denom)
    def __sub__(self, other):
        return Rational(self.numer*other.denom - self.denom*other.numer,
                        self.denom * other.denom)
    def __mul__(self, other):
        return Rational(self.numer*other.numer, self.denom * other.denom)
    def __truediv__(self, other):
        if (self.numer < 0 and other.numer < 0) or (self.numer > 0 and other.numer > 0):
            return Rational(abs(self.numer*other.denom), abs(self.denom * other.numer))
        else:
            return Rational(-1*abs(self.numer*other.denom), abs(self.denom * other.numer))
    def __abs__(self):
        return Rational(abs(self.numer),abs(self.denom))
    def __pow__(self, power):
        if type(power) is int and power >= 0:
            return Rational(self.numer ** power,self.denom ** power)
        elif type(power) is int and power < 0:
            return Rational(self.denom ** abs(power),self.numer ** abs(power))
        else:
            return self.numer ** power / self.denom ** power
    def __rpow__(self, base):
        return math.pow(base**self.numer, 1/self.denom)