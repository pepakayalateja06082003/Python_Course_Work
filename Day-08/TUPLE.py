Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
######################################################################
#                               TUPLE                                #
######################################################################

t = ()
t = tuple()
t = (1,2,3,4,5,6)
t
(1, 2, 3, 4, 5, 6)
t = (2)
t
2
t = (1,)
t
(1,)
t
(1,)
t=(1,2,2,2,2,2,)
t
(1, 2, 2, 2, 2, 2)
t = (1,23.4,"str"[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t = (1,23.4,"str"[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
TypeError: string indices must be integers, not 'tuple'
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>

###################


(1, 2, 3, 4, 5, 6)+(1, 2, 3, 4, 5, 6)
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

(1, 2, 3, 4, 5, 6) * 2
(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
 t[1]
 
SyntaxError: unexpected indent
t[1]
23.4
t[-1]
True
t[2]
'str'
t[3:7}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2})
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)

23.3 in t
False
'str' int
SyntaxError: invalid syntax
'str' in t
True
True in t
True
False in t
False
t =  (12,23,81,1,98,7,30,81,78,01,73,812,3,7,0,41)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
t =  (12,23,81,1,98,7,30,81,78,1,73,812,3,70,41)
sorted(t)
[1, 1, 3, 7, 12, 23, 30, 41, 70, 73, 78, 81, 81, 98, 812]
max(t)
812
min(t)
1
t
(12, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41)
t.index(23)
1
t.count(1)
2
sum(t)
1411
all((t))
True
any (t)
True
t
(12, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41)
a,d,d,g, = t
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a,d,d,g, = t
ValueError: too many values to unpack (expected 4, got 15)
a,d,g = t
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a,d,g = t
ValueError: too many values to unpack (expected 3, got 15)
t = 1,2,3
a ,b,c =t
t
(1, 2, 3)
t[2]
3
t[2].append[5]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    t[2].append[5]
AttributeError: 'int' object has no attribute 'append'
t[2].append(4)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t[2].append(4)
AttributeError: 'int' object has no attribute 'append'
t[1].append(2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t[1].append(2)
AttributeError: 'int' object has no attribute 'append'
t = 2, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41
t.[4].append[5]
SyntaxError: invalid syntax
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
########################################################################



#mu unor uni dyn he


#**Mutable, Immutable, Dynamic, Fixed Size (Non-Dynamic), Heterogeneous, Homogeneous**


#set


s = set()
type(s)
<class 'set'>
s = {12, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41}
s
{1, 98, 3, 70, 7, 41, 73, 12, 812, 78, 81, 23, 30}
s = {1,1,1,1,1,1}
s
{1}
sset()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    sset()
NameError: name 'sset' is not defined. Did you mean: 'set'?
+
s = set()
s.add(2)
s.add(3)
s.add("TEja")
s
{2, 3, 'TEja'}
s.add({1:1})
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.add({1:1})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(False)
s
{False, 2, 3, 'TEja'}



a
1

a = {10, 20, 30, 40}
b = {11, 10, 22, 30}

a - b
{40, 20}
 a- c
 
SyntaxError: unexpected indent
a - c
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a - c
TypeError: unsupported operand type(s) for -: 'set' and 'int'
a - d
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a - d
NameError: name 'd' is not defined. Did you mean: 'id'?
a - b
{40, 20}

a | b
{40, 10, 11, 20, 22, 30}
a & b
{10, 30}
b - a
{11, 22}


# {1}{1,2}


a
{40, 10, 20, 30}
 a> = {40,20}
 
SyntaxError: unexpected indent
a> = {40,20}
SyntaxError: invalid syntax
a >= {40,20}
True
n.isdisjoint(m)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    n.isdisjoint(m)
NameError: name 'n' is not defined
n.isdisjoint(a)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    n.isdisjoint(a)
NameError: name 'n' is not defined
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True


a = {12, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41}
a
{1, 98, 3, 70, 7, 41, 73, 12, 812, 78, 81, 23, 30}
sorted(a)
[1, 3, 7, 12, 23, 30, 41, 70, 73, 78, 81, 98, 812]
max(a)
812
min(a)
1
len(a)
13
a.index(a)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.index(a)
AttributeError: 'set' object has no attribute 'index'
a.index(1)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.index(1)
AttributeError: 'set' object has no attribute 'index'
all{12, 23, 81, 1, 98, 7, 30, 81, 78, 1, 73, 812, 3, 70, 41}
SyntaxError: invalid syntax
all(a)
True
any(a)
True
sum(a)
1329
a
{1, 98, 3, 70, 7, 41, 73, 12, 812, 78, 81, 23, 30}
>>> a
{1, 98, 3, 70, 7, 41, 73, 12, 812, 78, 81, 23, 30}
>>> a={10, 20, 30, 40}
>>> b  = a
>>> b
{40, 10, 20, 30}
>>> b.add(3)
>>> a
{3, 40, 10, 20, 30}
>>> b
{3, 40, 10, 20, 30}
>>> c= a.copy()
>>> c
{3, 20, 40, 10, 30}
>>> c.add(5)
>>> c
{3, 20, 5, 40, 10, 30}
>>> a
{3, 40, 10, 20, 30}
>>> 
>>> 
>>> a
{3, 40, 10, 20, 30}
>>> a.add(5)
>>> a
{3, 5, 40, 10, 20, 30}
>>> a.add({10, 20, 30, 40})
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    a.add({10, 20, 30, 40})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
>>> a.update({10, 20, 30, 40})
... 
>>> a.update({10, 20, 30, 40})
>>> 
>>> a
{3, 5, 40, 10, 20, 30}
>>> a.pop
<built-in method pop of set object at 0x000001599E1D33E0>
>>> a.pop()
3
>>> a
{5, 40, 10, 20, 30}
>>> a.remove(10)
>>> a
{5, 40, 20, 30}
>>> a
{5, 40, 20, 30}
>>> a.clear()
>>> a
set()
>>> a = frozenset({1,1,1,11,1,1,1,1})
>>> a
frozenset({1, 11})
