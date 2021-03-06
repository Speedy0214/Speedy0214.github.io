---
layout: post
title: " Divid and Conquer —— Recurrence Relation examples"
categories: [ Data Structures and Algorithms ]
date: 2019-10-07
---

### Notes in learning [Data Structures and Algorithms course](https://dsa.cs.tsinghua.edu.cn/~deng/ds/dsacpp/dsacpp.3rd_edn.pdf)  
##### 1. Recurrence Relation
<span> a.$T(n) = 2*T(n/2) + O(1)$ ; base case $T(1) = O(1)$ <span>
> $$ T(n) = 2*T(n/2) + c_{1} $$  
> <span class="note">Build Geometric Sequences</span>   
> $$ T(n) + c_{1} = 2*(T(n/2) + c_{1}) = 2^{log(n)(T_{1} + c_{1})} $$   
> $$ T(n) = O(n) $$  

<span>b. $$ T(n) = 2*T(n/2) + O(1) ; base case T(3) = O(3), T(2)=O(1) $$ </span>

> $$ T(n) + 2 = 2*(T(n/2) + 2) $$  
> if only T(2) in base cases:  
> $$ T(n) + 2 = 2^{log(n) - 1}*(T(2) + 2) $$  
> $$  T(n) = 3n/2 -2 $$  
> if only T(3) in base cases:  
> $$  T(n) + 2 = 3^{log(n) - 1}*(T(3) + 2) $$  
> $$  T(n) = 5n/2 -2 $$  























---


---
<h2>Reference</h2>
