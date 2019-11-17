---
layout: post
title: "a introduction to computer"
categories: [Computer]
date: 2019-11-11
---

### Table of content  
>1. History of computer 
>2. 
>3. 

-------

### 1 History    
1.1. ENIAC: 1946, transistor(vacuum tube, electron tube)
![electron tube](/assets/computer/electron_tube1.png)
![triode](/assets/computer/triode.png)
1.2. Transistor  
![transistor_symbol](/assets/computer/transistor_symbol.png)
![transistor](/assets/computer/transistor.png)

1.3. History  

| year | technology | speed(/sec) |
| ---  |   ----     |  ---  |
| 1946~1957 | triode | ~40k   |
| 1958~ 1964 | transistor | ~200k |
| 1965~1971  | integrated circuit | ~1 million|
| 1972～1977 | Large Scale integrated circuit | ~10 million|
| 1978~ now| Very large-scale integrated circuit | ~1 billion | 

> **Moore's Law** : Moore's law is the observation that the number of transistors in a dense integrated circuit doubles about every two years.
> **Microprocessor** 
> **Memory Devices** : ROM RAM 

### 2 build a simple computer
2.1 **Computer --  arithmetic , logical operations , storing data.**
> Logical operations: and, or , Xor (exclusive or)
> Truth table: A truth table is a mathematical table used in logic—specifically in connection with Boolean algebra, boolean functions, and propositional calculus—which sets out the functional values of logical expressions on each of their functional arguments, that is, for each combination of values taken by their logical variables.

>And :  


| In1| In2 | Out|
|--:|--:|--:|
| 1| 1| 1|
| 0| 1| 0|
| 1| 0| 0|
| 0| 0| 0|

>X or : 


| In1| In2 | Out|
|--:|--:|--:|
| 1| 1| 0|
| 0| 1| 1|
| 1| 0| 1|
| 0| 0| 0|

> Arithmetic operations: 

> Add 
$$
\left \{ 
\begin{array}{c}
1 + 1 = 10 \\ 
1 + 0 = 01 \\ 
0 + 1 = 01 \\
0 + 0 = 00
\end{array}
\right.
$$
>> "add" = "and" + "Xor"
![add](/assets/computer/add_0.png)
>> 
$$
\left[  \begin{array}  {c} 
 & \cdots A_{i+1}A_iA_{i-1}\cdots \\
+& \cdots B_{i+1}B_iB_{i-1}\cdots \\
\hline
 & \cdots S_{i+1}S_iS_{i-1}\cdots
\end{array}  \right]
$$
>> INPUT : $A_i, B_i, C_{i-1}$
>> OUTPUT : $S_i, C_i$
![add](/assets/computer/add_0.png)

>add  
![add](/assets/computer/add__.png)

> Memory
![ROM](/assets/computer/ROM__.png)
<h2>Reference</h2>    

[Wikipedia](https://www.wikipedia.org)