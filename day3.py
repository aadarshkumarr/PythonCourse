"""
Errors
# SyntaxError
-> print "hello"
SyntaxError:--------- wrong syntex input
print("hello")

# IndexError
-> l=[2,5,6]
l[3]
IndexError:-------------- 3 id put of bound as list index start with 0

# ModuleNotFoundError
-> import wrongmodule
ModuleNotFoundError:---------- wrong module name enter

# KeyErorr
-> d{'1':"qwe",'2':"ryd"}
d[3]
KeyError:---  as key 3 is not present

# ImportError
-> from math import cube
ImportError:--- as math library is not installed yet

# StopIterationError
-> it=iter([1,2,3)]
next(it)
1
next(it)
2
next(it)
3
next(it)
StopItration:--- as 3 is the last Itration

# TypeError
-> "12"+3
TypeError:------ as "12 is string and 3 is int

# ValueError
-> int("dtd")
valueError:---- as dtd is not integer

# NameError
calling not decrared variable

# ZeroDivisionError
as a number divide by 0

# KeyboardInterruptError
as the program stoped using ctrl+c while running

# IndentationError
python use spaces as block of code if thse spaces places in correctly the program will give IndentationError
"""