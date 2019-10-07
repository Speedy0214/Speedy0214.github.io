---
layout: post
title: " Data Structures and Algorithms"
categories: [ Data Structures and Algorithms ]
date: 2019-10-07
---

# Notes in learning [Data Structures and Algorithms course](https://dsa.cs.tsinghua.edu.cn/~deng/ds/dsacpp/dsacpp.3rd_edn.pdf)

### 1.Recurrence Relation

a. $$ T(n) = 2*T(n/2) + O(1) ; base case T(1) = O(1) $$  
>> SOLUTION   
>> $$T(n)     = 2*T(n/2) + c_{1}$$  
>> Build Geometric Sequences  
>> $$ T(n) + c_{1} = 2*(T(n/2) + c_{1}) = 2^{log(n)(T_{1} + c_{1})} $$  
>> $$ T(n) = O(n) $$  

b. $$ T(n) = 2*T(n/2) + O(1) ; base case T(3) = O(3), T(2)=O(1) $$
>> solution  
$$T(n) + 2 = 2*(T(n/2) + 2) $$
if only T(2) in base cases:
$$  T(n) + 2 = 2^{log(n) - 1}*(T(2) + 2) $$
$$  T(n) = 3n/2 -2 $$























---


---
<h2>Reference</h2>
