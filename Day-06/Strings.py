Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#1.Concatentation.

F1 = "Teja"
F2 = "Pep"
F1 + F2
'TejaPep'

F1 * 10
'TejaTejaTejaTejaTejaTejaTejaTejaTejaTeja'


type(F1)
<class 'str'>


# 2.indexing

# tyes - & + Two types + start (0) .. 1 is (-)

# axis large set and picking name in a set.

### name[:8] or [8:12].......[12:23]


### name[:8] or [8:12].......[12:23]

name = " SAI Teja KUMAR SHIVA "
name
' SAI Teja KUMAR SHIVA '
name(3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name(3)
TypeError: 'str' object is not callable
name(:3)
SyntaxError: invalid syntax
name[:3]
' SA'
name[:3:4]
' '
name[-5:]
'HIVA '
name[4:]
' Teja KUMAR SHIVA '
name[:4]
' SAI'
name[4:3]
''
name[3:4]
'I'
name[-1:-4:-6]
' '
name[::-1]
' AVIHS RAMUK ajeT IAS '
name =  " sai  teja "
ord("a")
97
chr(10)
'\n'
chr(97)
'a'
sorted(name)
[' ', ' ', ' ', ' ', 'a', 'a', 'e', 'i', 'j', 's', 't']
max(name)
't'
min(name)
' '
s="python is high "
s.upper()
'PYTHON IS HIGH '
s.lower()
'python is high '
s.swapcase()
'PYTHON IS HIGH '
s.capitalize()
'Python is high '
s.title()
'Python Is High '
s  = " SyntaxError invalid syntax "
s.center(5,"---")
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s.center(5,"---")
TypeError: The fill character must be exactly one character long
>>> s.center(5, '___'0
...          
SyntaxError: '(' was never closed
>>> s.center(5, '___')
...          
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.center(5, '___')
TypeError: The fill character must be exactly one character long
>>> "123".zfill(4)
...          
'0123'
>>> s.rjust(40,".")
...          
'............ SyntaxError invalid syntax '
>>> s.center(40,".")
...          
'...... SyntaxError invalid syntax ......'
>>> s.ljust(100,"$")
...          
' SyntaxError invalid syntax $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
>>> s.find(a)
...          
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s.find(a)
NameError: name 'a' is not defined
>>> s.find("a")
...          
5
>>> s.count("A")
...          
0
>>> s.count("s")
...          
1
>>> s.count
...          
<built-in method count of str object at 0x000001E6C4EFEBF0>
>>> s.count("S","a")
...          
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.count("S","a")
TypeError: slice indices must be integers or None or have an __index__ method
>>> s.count("S" "a")
...          
0
>>> s.count("s" "a")
...          
0
>>> s.find("x")
...          
6
