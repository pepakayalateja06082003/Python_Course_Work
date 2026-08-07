Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#### Input Formatting

#=== comma separation

a = 10
b = 16
c = "hi"

print(a,c,b)
10 hi 16

print ("a=" a , " b=" c , "c=" b )
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print ("a=" , a , " b="  , c , "c=" , b )
a= 10  b= hi c= 16

print ("a=" , a , " b="  , c , "c=" , b sep= " " )
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print ("a=" , a , " b="  , c , "c=" , b , sep = " " )
a= 10  b= hi c= 16
print ("a=" , a , " b="  , c , "c=" , b  , sep="/n")
a=/n10/n b=/nhi/nc=/n16
print ("a=" , a , " b="  , c , "c=" , b, sep = "\n" )
a=
10
 b=
hi
c=
16
>>> print ("a=" , a , " b="  , c , "c=" , b, sep = "/t" )
a=/t10/t b=/thi/tc=/t16
>>> 
>>> print ("a=" , a , " b="  , c , "c=" , b, sep = "\t" )
... 
a=	10	 b=	hi	c=	16
>>> print ("a=" , a , " b="  , c , "c=" , b, sep = "\n\n" )
a=

10

 b=

hi

c=

16
>>> print ("a=" , a , " b="  , c , "c=" , b, sep = "\t" end='a')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print ("a=" , a , " b="  , c , "c=" , b, sep = "\t" , end = " as ")
a=	10	 b=	hi	c=	16 as 
>>> print (f'a = {a} b = {b} c = {c} ')
a = 10 b = 16 c = hi 
>>> a = 10 b = 16 c = hi
SyntaxError: invalid syntax
>>> 
>>> ####### Print (f'a = {a} b = {b} c = {c} ') --------(f string )
>>> 
>>> 
>>> rint (f'a = %d b = %f c = %s ' % (a,b,c))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    rint (f'a = %d b = %f c = %s ' % (a,b,c))
NameError: name 'rint' is not defined. Did you mean: 'print'?
>>> print ('a = %d b = %f c = %s ' % (a,b,c))
a = 10 b = 16.000000 c = hi 
>>> a = 10 b = 16.000000 c = hi
SyntaxError: invalid syntax
>>> print ('a = %d b = %f c = %s ' % format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print ('a = %d b = %f c = %s ' % format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
>>> TypeError: format expected at most 2 arguments, got 3
SyntaxError: invalid syntax
>>> print ('a = {a} b = {b} c = {c}' %.format(a,b,c))
SyntaxError: invalid syntax
>>> print ('a = {a} b = {b} c = {c}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print ('a = {a} b = {b} c = {c}'.format(a,b,c))
KeyError: 'a'
>>> print ('a = {0} b = {2} c = {1}' .format(a,b,c))
a = 10 b = hi c = 16
