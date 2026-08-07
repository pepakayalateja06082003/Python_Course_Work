Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #=======Python Operators====#
>>> 
>>> 1. Arithmetic Operators
... 2. Comparison Operators
... 3. Assignment Operators
... 4. Logical Operators
... 5. Membership Operators
... 6. Identity Operators
... 7. Bitwise Operators
... 
SyntaxError: invalid syntax
>>> #===============================#
>>> 
>>> #1. Arithmetic Operators
>>> | Operator       | Symbol | Example  | Output | Purpose                  |
... | -------------- | ------ | -------- | ------ | ------------------------ |
... | Addition       | `+`    | `5 + 3`  | `8`    | Adds values              |
... | Subtraction    | `-`    | `10 - 4` | `6`    | Subtracts values         |
... | Multiplication | `*`    | `6 * 2`  | `12`   | Multiplies values        |
... | Division       | `/`    | `9 / 2`  | `4.5`  | Returns float result     |
... | Floor Division | `//`   | `9 // 2` | `4`    | Returns integer quotient |
... | Modulus        | `%`    | `10 % 3` | `1`    | Returns remainder        |
... | Exponentiation | `**`   | `2 ** 3` | `8`    | Power operation          |
... 
SyntaxError: invalid syntax
>>> #===============================================================================#
>>> 
>>> # Testing
>>> 
>>> a = 22
>>> b = 33
>>> 
>>> a+b
55
>>> b-a
11
>>> a*b
726
>>> a**b
199502557355935975909450298726667414302359552
>>> a/
SyntaxError: invalid syntax
>>> a/b
0.6666666666666666
>>> a//b
0
>>> a%b
22
>>> #========================================================================================
>>> 
>>> 
>>> ##=========================================================================================
>>> 
>>> # 2. Comparison Operators
| Operator         | Symbol | Example  | Output | Purpose           |
| ---------------- | ------ | -------- | ------ | ----------------- |
| Equal            | `==`   | `5 == 5` | `True` | Checks equality   |
| Not Equal        | `!=`   | `5 != 3` | `True` | Checks inequality |
| Greater Than     | `>`    | `7 > 3`  | `True` | Greater value     |
| Less Than        | `<`    | `3 < 7`  | `True` | Smaller value     |
| Greater or Equal | `>=`   | `5 >= 5` | `True` | Greater or equal  |
| Less or Equal    | `<=`   | `3 <= 5` | `True` | Smaller or equal  |
# 2. Comparison Operators
SyntaxError: invalid syntax
a=12
b=13

a==b
False
a!=b
True
a>b
False
a<b
True
a<=b
True
a>=a
True
a==a
True
b==a
False
#==================================================================================================




#3. Assignment Operators

| Operator              | Symbol | Example          | Equivalent               |
| --------------------- | ------ | ---------------- | ------------------------ |
| Assign                | `=`    | `x = 5`          | Assign value             |
| Add & Assign          | `+=`   | `x += 3`         | `x = x + 3`              |
| Subtract & Assign     | `-=`   | `x -= 2`         | `x = x - 2`              |
| Multiply & Assign     | `*=`   | `x *= 4`         | `x = x * 4`              |
| Divide & Assign       | `/=`   | `x /= 2`         | `x = x / 2`              |
| Floor Divide & Assign | `//=`  | `x //= 3`        | `x = x // 3`             |
| Modulus & Assign      | `%=`   | `x %= 2`         | `x = x % 2`              |
| Power & Assign        | `**=`  | `x **= 3`        | `x = x ** 3`             |
| Bitwise AND Assign    | `&=`   | `x &= 3`         | `x = x & 3`              |
| Bitwise OR Assign     | `\|=`  | `x \|= 3`        | `x = x \| 3`             |
| Bitwise XOR Assign    | `^=`   | `x ^= 3`         | `x = x ^ 3`              |
| Left Shift Assign     | `<<=`  | `x <<= 2`        | `x = x << 2`             |
| Right Shift Assign    | `>>=`  | `x >>= 2`        | `x = x >> 2`             |
| Walrus                | `:=`   | `print(x := 10)` | Assign inside expression |

SyntaxError: invalid syntax


a = 12
b = 2

a += 1
a
13
a -= 2
a *= 1
a
11
a /= 2
a //= b
a
2.0
a %= 2
a
0.0
a **= 1
a &= 1
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a &= 1
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
a %= 1
a >>= 2
a
0.0
a=1 2
SyntaxError: invalid syntax
a 12
SyntaxError: invalid syntax
a=12
a <<=2
a
48
#===========================================================

#4. Logical Operators
'''
Operator	Symbol	Meaning	Returns True When
AND	and	Both conditions	Both are True
OR	or	Any one condition	At least one is True
NOT	not	Reverse result	True ↔ False

Truth Table (AND)
A	B	A and B
True	True	True
True	False	False
False	True	False
False	False	False

Truth Table (OR)
A	B	A or B
True	True	True
True	False	True
False	True	True
False	False	False

Truth Table (NOT)
A	not A
True	False
False	True

'''


a = 12
b = 13


a and b
13
a = True
b = False

a or b
True

a or a
True

   

a and a
True


a not a
SyntaxError: invalid syntax
a not
SyntaxError: invalid syntax
a = True
a not
SyntaxError: invalid syntax
not a==a
False
not a!=a
True
#======================================

#5. Membership Operators

Operator	Symbol	Example	Output	Purpose
In	in	"a" in "apple"	True	Value exists
Not In	not in	"x" not in "apple"	True	Value doesn't exist
SyntaxError: unterminated string literal (detected at line 5)

| Operator | Symbol   | Example              | Output | Purpose             |
| -------- | -------- | -------------------- | ------ | ------------------- |
| In       | `in`     | `"a" in "apple"`     | True   | Value exists        |
| Not In   | `not in` | `"x" not in "apple"` | True   | Value doesn't exist |

SyntaxError: unterminated string literal (detected at line 4)





a = 12
b = 13

a in b
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a in b
TypeError: argument of type 'int' is not a container or iterable
a =[ 1, 2,1 ,3]
b = [ 1, 2,1 ,3]

a  in b
False
 a in a
 
SyntaxError: unexpected indent
a in a
False
 b in a
 
SyntaxError: unexpected indent
b in a
False

a  not in b
True
#======================================================================

#6. Identity Operators
'''
| Operator | Symbol   | Example      | Purpose           |
| -------- | -------- | ------------ | ----------------- |
| Is       | `is`     | `a is b`     | Same object       |
| Is Not   | `is not` | `a is not c` | Different objects |

'''
a = 1
b = 2
a is b
False
a is not b
True
a is a
True
b is b
True
True
True

#===================================================================

#7. Bitwise Operators

"""
| Operator    | Symbol | Example  | Output | Purpose       |
| ----------- | ------ | -------- | ------ | ------------- |
| AND         | `&`    | `5 & 3`  | `1`    | Bitwise AND   |
| OR          | `\|`   | `5 \| 3` | `7`    | Bitwise OR    |
| XOR         | `^`    | `5 ^ 3`  | `6`    | Bitwise XOR   |
| NOT         | `~`    | `~5`     | `-6`   | Bitwise NOT   |
| Left Shift  | `<<`   | `5 << 1` | `10`   | Multiply by 2 |
| Right Shift | `>>`   | `5 >> 1` | `2`    | Divide by 2   |



| A | B | A & B | A | B | A ^ B | ~A |
| - | - | ----- | ----- | ----- | -- |
| 0 | 0 | 0     | 0     | 0     | 1  |
| 0 | 1 | 0     | 1     | 1     | 1  |
| 1 | 0 | 0     | 1     | 1     | 0  |
| 1 | 1 | 1     | 1     | 0     | 0  |



"""




a = 1
b = 2

a & b
0
a & a
1
11 & 12
8
11 | 15
15
11 ^ 12
7
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 16>>2
4
>>> ~14
-15
>>> ~78
-79
>>> ~23
-24
~65
-66
~32
-33
