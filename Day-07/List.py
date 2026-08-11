Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
########################################################################
#                           LIST                                       #
########################################################################


l = []

l = list()
type(l)
<class 'list'>

l = [1, "a"], True, False, {4, 5, 6}, {"id": 101}, [7, 8, 9], "world"

l
([1, 'a'], True, False, {4, 5, 6}, {'id': 101}, [7, 8, 9], 'world')

l = [1,1,1,1]
l
[1, 1, 1, 1]

############################################################################
#                               CONCATIONS                                 #
############################################################################


a = [1,11,12,13,14]
b = [21,1,21,32,34]

a+b
[1, 11, 12, 13, 14, 21, 1, 21, 32, 34]
a*2
[1, 11, 12, 13, 14, 1, 11, 12, 13, 14]
a[2]
12
a[9]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a[9]
IndexError: list index out of range
a[3]
13

a[-1]
14
a[-2]
13
a
[1, 11, 12, 13, 14]
a[1:14]
[11, 12, 13, 14]
a[2:2]
[]
a[1::2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a=[1::2]
SyntaxError: invalid syntax
a[1::2]
[11, 13]
a
[1, 11, 12, 13, 14]
11 in a
True
121 in a
False

####################################################################################
#                                    LIST METHODS                                  #
####################################################################################

#  max , min , sorted , len.....only 4types





a = [ 25, 65, 55,99, 66, 78]
a
[25, 65, 55, 99, 66, 78]
max(a)
99
min(b)
1
sorted(a)
[25, 55, 65, 66, 78, 99]
len(a)
6

id(a)
2729034552256

a[0]
25
a(-1) = 221
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
a[-1]=2221
a
[25, 65, 55, 99, 66, 2221]
a.append(55)
a
[25, 65, 55, 99, 66, 2221, 55]
a.append
<built-in method append of list object at 0x0000027B672293C0>
a.append(60)
a
[25, 65, 55, 99, 66, 2221, 55, 60]
a.insert(1,66)
a
[25, 66, 65, 55, 99, 66, 2221, 55, 60]
a.extend([1,1,1,11,2,2,1])
a
[25, 66, 65, 55, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2, 1]
a.pop
<built-in method pop of list object at 0x0000027B672293C0>
a.pop()
1
a
[25, 66, 65, 55, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
del[0:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
del(0:3)
SyntaxError: invalid syntax
del a[1:3]
a
[25, 55, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
a.remove(55)
a
[25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
a.clear()
a
[]









###########################################################################################################################

"#"*50
'##################################################'




























a = index(2)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a = index(2)
NameError: name 'index' is not defined












... 
>>> a = [25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
>>> a
[25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
>>>  a =index(2)
...  
SyntaxError: unexpected indent
>>> a = index(2)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a = index(2)
NameError: name 'index' is not defined
>>> a.index(2)
10
>>> 
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count(1)
3
>>> b.append(12)
>>> b
[21, 1, 21, 32, 34, 12]
>>> c = a.copy()
>>> c.append(1111)
>>> a
[25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2]
>>> c
[25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2, 1111]
>>> [25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2, 1111]
[25, 99, 66, 2221, 55, 60, 1, 1, 1, 11, 2, 2, 1111]
>>> 
>>> any([ True, "" ,1,(),{}])
True
>>> 
>>> any([ False, "" ,1,(),{}])
True
>>> any([ , "" ,0,(),{}])
... 
SyntaxError: invalid syntax
>>> any([ False , "" ,0,(),{}])
... 
False
>>> all([ True, "" ,1,(),{}])
False
>>> 
>>> 
>>> a.sort()
>>> a
[1, 1, 1, 2, 2, 11, 25, 55, 60, 66, 99, 2221]
>>> a.reverse()
>>> a
[2221, 99, 66, 60, 55, 25, 11, 2, 2, 1, 1, 1]
