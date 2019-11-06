---
layout: post
title: "a python tutorial"
categories: [PY-TUTORIAL]
date: 2019-11-06
---

Table of content  
1. Interpreter(解释器)  
Cpython  
PyPy  
Jython  
IronPython

1 Interpreter  
1.1 Python interpreters

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
Standard Encodings
Codec | Aliases | Languages
-| -| -
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
gb2312|chinese, csiso58gb231280, euc-cn, euccn, eucgb2312-cn, gb2312-1980, gb2312-80, iso-ir-58|Simplified Chinese
gbk|936, cp936, ms936|Unified Chinese
gb18030|gb18030-2000|Unified Chinese
hz|hzgb, hz-gb, hz-gb-2312|Simplified Chinese




---


---
<h2>Reference</h2>

[Python Interpreter]( https://docs.python.org/3/tutorial/interpreter.html )
