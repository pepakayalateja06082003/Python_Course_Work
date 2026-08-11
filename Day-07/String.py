Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '          Hello World              '
s
'          Hello World              '
s.strip()
'Hello World'
s.lstrip()
'Hello World              '
s.rstript()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.rstript()
AttributeError: 'str' object has no attribute 'rstript'. Did you mean: 'rstrip'?
s.rstrip()
'          Hello World'
s.replace('','')
'          Hello World              '
'          Hello World              '
'          Hello World              '
s.replace(' ','')
'HelloWorld'
s.replace('',' ')
'                     H e l l o   W o r l d                             '
'                     H e l l o   W o r l d                             '
'                     H e l l o   W o r l d                             '

#===Splitting and joining

#===Splitting and joining


S =  " Codegnan is a leading IT training institute dedicated to transforming students into skilled professionals ready for the tech industry "
S
' Codegnan is a leading IT training institute dedicated to transforming students into skilled professionals ready for the tech industry '
S.split(' ')
['', 'Codegnan', 'is', 'a', 'leading', 'IT', 'training', 'institute', 'dedicated', 'to', 'transforming', 'students', 'into', 'skilled', 'professionals', 'ready', 'for', 'the', 'tech', 'industry', '']
S.split('_',2)
[' Codegnan is a leading IT training institute dedicated to transforming students into skilled professionals ready for the tech industry ']
s.rsplit
<built-in method rsplit of str object at 0x000001AD2F116600>
S.rsplit('-',2)
[' Codegnan is a leading IT training institute dedicated to transforming students into skilled professionals ready for the tech industry ']
l = ''' py '''
l= '' py
SyntaxError: invalid syntax

l = ''' py
ja
my
fl
'''
l
' py\nja\nmy\nfl\n'
l.splitlines
<built-in method splitlines of str object at 0x000001AD2F133D70>
l.splitlines()
[' py', 'ja', 'my', 'fl']
c = "Codegnan is a leading IT training institute"
" ".join(c)
'C o d e g n a n   i s   a   l e a d i n g   I T   t r a i n i n g   i n s t i t u t e'
''.join(c)
'Codegnan is a leading IT training institute'
'#'.join(c)
'C#o#d#e#g#n#a#n# #i#s# #a# #l#e#a#d#i#n#g# #I#T# #t#r#a#i#n#i#n#g# #i#n#s#t#i#t#u#t#e'
'--'.join(c)
'C--o--d--e--g--n--a--n-- --i--s-- --a-- --l--e--a--d--i--n--g-- --I--T-- --t--r--a--i--n--i--n--g-- --i--n--s--t--i--t--u--t--e'
'C--o--d--e--g--n--a--n-- --i--s-- --a-- --l--e--a--d--i--n--g-- --I--T-- --t--r--a--i--n--i--n--g-- --i--n--s--t--i--t--u--t--e'
'C--o--d--e--g--n--a--n-- --i--s-- --a-- --l--e--a--d--i--n--g-- --I--T-- --t--r--a--i--n--i--n--g-- --i--n--s--t--i--t--u--t--e'

'-'.join({'1','2','3'})
'3-1-2'


a = "sai.p"
a.partition('.')
('sai', '.', 'p')
a.rpartition('.')
('sai', '.', 'p')
('sai', '.', 'p')
('sai', '.', 'p')

############# ============== String testing ==============



a = "string.png"
a
'string.png'

a.startswith("str")
True
a.startswith("list")
False
a.endswith("png")
True


"Teja.Pep".islower()
False

M = 8886221973



"Teja.Pep".isupper()
False
"sdfg".islower()
True

"My noo 8886221973 "
'My noo 8886221973 '

"My noo 8886221973 ".isupper()
False

"My noo 8886221973 @#%$ ".isupper()

False
"myname".issupper()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    "myname".issupper()
AttributeError: 'str' object has no attribute 'issupper'. Did you mean: 'isupper'?
>>> "myname".isupper()
False
>>> "PSA123!@#"isupper()
SyntaxError: invalid syntax
>>> "PSA123!@#".isupper()
True
>>> "PSA123!@#"isalpha()
SyntaxError: invalid syntax
>>> "PSA123!@#".isalpha()
False
>>> "PSA123!@#".isalnum()
False
>>> "PSA123!@#".isnum()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    "PSA123!@#".isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> "PSA123!@#".isalspace()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    "PSA123!@#".isalspace()
AttributeError: 'str' object has no attribute 'isalspace'. Did you mean: 'isspace'?
>>> "PSA123!@#".isspace()
False
>>> "PSA123!@#".istitle()
False
>>> "PSA123!@#".isindentifier()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    "PSA123!@#".isindentifier()
AttributeError: 'str' object has no attribute 'isindentifier'. Did you mean: 'isidentifier'?
>>> "PSA123!@#".isidentifier()
False
>>> 
>>> "in".isidentifier()
True
>>> 
>>> a.partition(".")
('string', '.', 'png')
>>> 
>>> 
>>> 
>>> "12345667".isdecimal()
True
>>> 
>>> "ERHBSJBJK123123".isdecimal
<built-in method isdecimal of str object at 0x000001AD2F14B730>
>>> "ERHBSJBJK123123".isdecimal()
False
>>> '223123'.isdigit()
True
