from this import d


# h=d(0.7+0.2)
# h=d(0.7)+d(0.2)
# h=d('0.7')+d("0.2")
# print(h)#TypeError:'dicvt' object is not callqble
# a=0.7; b=0.2
# c=a+b
# print(c)#0.899999999999999
# print("%.1f" %c)#0.9
# print(7/0)#ZeroDivisionError: division by zero
# from fractions import Fraction as f
# # a=f(1,0)
# a=f(1,1)
# print(a)#1
# a=f(1,5)
# print(a)#1/5
# b=f(2)
# print(b)#2
# d=f(0,5)
# print(d)#0
# v=f(5,25)
# print(v)#1/5
# a=1_23
# print(a,type(a))#123 int
# b=1_3.0
# print(b,type(b))#13.0 float
# c=1._03#SyntaxError:inval;id decimal literal
# d=1_0.3#SyntaxError:inval;id decimal literal
# a=5; b=4.6
# print(a,type(a))
# print(b,type(b))
# print(isinstance(a, int))#True
# print(isinstance(a,float))#Flase
# print(isinstance(a,bool))#Flase
# print(isinstance(b,float))#True
# c=4j
# print(c,type(c))#complex
# d=1+3j
# print(d,type(d))#complex
# print(isinstance(d,complex))#True
from fractions import Fraction as F
# print(F(6,2))#3
# print(F(2,5))#2/5
# print(F('2.5'))#5/2
# print(F("2.5"))#5/2
# y=F(4.5)
# print(y,type(y))#9/2
# print(F(5,0))#ZeroDivision:Fraction(5,0)
# b=5/0#ZeroDivisionError: division by zero
# v=F(5,20)
# print(v)#1/4
g=2+3j
print(g,type(g))#complex
print(g.real)#2.0
print(g.imag)#3.
h=7*2.3j
print(h,type(h))#complex
print(h.real)#
print(h.imag)
