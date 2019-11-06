---
layout: post
title: "a python tutorial - 1"
categories: [PY-TUTORIAL]
date: 2019-11-06
---

### Table of content  
1. Interpreter(解释器)  
2. Basic Data Types
3. Control Flow


-------

### 1 Interpreter  
1.1 Python interpreters  
>Cpython  
PyPy  
Jython  
IronPython

1.2 Argument Passing and Interactive Mode  

```python
    $ python3 hello.py arg0 arg1 arg 2 
      script name and add args are turned into a list of strings and assigned to sys.argv
      sys.argv = ["hello", arg0, arg1, arg2]
```
```python
    $ python -m package
      note: interpreter execute __main__.py module
    $ python -c "print(1)
      print(2)"
```
1.2 Source Code Encoding
```
    # -*- coding: encoding -*-
```

>Standard Encodings  

Codec | Aliases | Languages
-:| -:| -:
ascii | 646, us-ascii | English
big5 | big5-tw, csbig5 |Traditional Chinese
utf_32 | U32 utf32 |all languages
utf_32_be | UTF-32BE |all languages
utf_32_le| UTF-32LE|all languages
utf_16|U16, utf16|all languages
utf_16_be|UTF-16BE|all languages
utf_16_le|UTF-16LE|all languages
utf_7|U7, unicode-1-1-utf-7|all languages
utf_8|U8, UTF, utf8, cp65001|all languages
utf_8_sig| |all languages
gb2312|chinese, csiso58gb231280..|Simplified Chinese
gbk|936, cp936, ms936|Unified Chinese
gb18030|gb18030-2000|Unified Chinese
hz|hzgb, hz-gb, hz-gb-2312|Simplified Chinese


------------

### 2 Basic Data Types  
2.1 Numbers  
> int  
  float  
  Decimal  
  Fraction  
  Complex numbers  

2.2 Strings 
> interactive mode  
```python
    >>> 'spam eggs'  # single quotes
        'spam eggs'
    >>> 'doesn\'t'  # use \' to escape the single  quote...
        "doesn't"
    >>> "doesn't"  # ...or use double quotes instead "doesn't"
    >>> '"Yes," they said.'
        '"Yes," they said.'
    >>> "\"Yes,\" they said."
        '"Yes," they said.'
    >>> '"Isn\'t," they said.'
        '"Isn\'t," they said.'
```
> use print()
```python
    >>> '"Isn\'t," they said.'
        '"Isn\'t," they said.'
    >>> print('"Isn\'t," they said.')
        "Isn't," they said.
    >>> s = 'First line.\nSecond line.'  # \n means newline
    >>> s  # without print(), \n is included in the output
        'First line.\nSecond line.'
    >>> print(s)  # with print(), \n produces a new line
        First line.
        Second line.
```
> If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
```python
    >>> print('C:\some\name')  # here \n means newline!
        C:\some
            ame
    >>> print(r'C:\some\name')  # note the r before the quote
        C:\some\name
```
> span multiple lines
```python
    print("""\
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
    """)  
```  
```
    Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
```
> operator  
```python
    >>> 3 * 'un' + 'ium'
    'unununium'
```  
> automatically concatenated
```python
    >>> 'Py' 'thon'
        'Python'
    >>> text = ('Put several strings within parentheses '
    ...         'to have them joined together.')
    >>> text
        'Put several strings within parentheses to have them joined together.'
```  

> indexing and slicing
```python
    >>> word = 'Python'
    >>> word[0]  # character in position 0
        'P'
    >>> word[5]  # character in position 5
        'n'
    >>> word[-2]  # second-last character
        'o'
    >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
    'Py'
    >>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
    'tho'
    >>> word[42]  # the word only has 6 characters
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: string index out of range
    >>> word[4:42]
    'on'
    >>> word[42:]
    ''
```
> Python strings cannot be changed — they are immutable.  

2.3 Lists
>compound data types  
> operations \+, \*  
> mutable type  
> append vs extend

2.4 Dicts 


### 3 Control Flow  
3.1 while Statements  
3.2 if Statements  
3.3 for Statements  
3.4 break and continue Statements  
3.5 pass Statements  
3.6 Defining Functions  
3.6.1 Default Argument Values  
>**Important warning:** The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

```python

    def f(a, L=[]):
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))

    [1]
    [1, 2]
    [1, 2, 3]
```
>If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
```python
    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L
```

3.6.2 Keyword Arguments  
>In a function call, keyword arguments must follow positional arguments.   
>When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.)  
3.6.3  Special parameters  
```python 
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```
>where / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.  
3.6.4 Arbitrary Argument Lists
```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```
3.6.5 Unpacking Arguments
```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]

>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
```
3.6.6 Lambda Expressions
3.6.7 Documentation Strings
3.6.8 Function Annotations
```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```
---



---
<h2>Reference</h2>

[Python Interpreter]( https://docs.python.org/3/tutorial )
