---
layout: post
title: "Chapter2 - Transformations and Expectations"
categories: [STATISTICS-TUTORIAL]
date: 2019-11-26
---

### Table of content  
>1. Distributions of Functions of a Random Variable
>2.

-------
   
1.1 Distributions of Functions of a Random Variable

If X is a random variable with cdf $F_X(x)$, then any function of $X$, say $g(X)$, is also a random variable. Often g(X) is interest itself and we write $Y = g(X)$ to denote the new random variable $g(X)$. Since $Y$ is a function of $X$, so can describe the probabilistic behavior of Y in terms of that of $X$. That is , for an set $A$,
$$ P(Y \in A) = P(g(X) \in A),$$
showing that the distribution of $Y$ depends on the functions $F_X$ and g.
Formally, if writing $y = g(x)$, the function $g(x)$ defines a mapping from the original sample space $S_1$ to a new sample space, that is ,$$ g(x): S_1 \to S_2\ .$$
If associate with g an inverse mapping, denoted by $g^{-1}$, which is a mapping from subsets of $S_2$ to subsets of $S_1$, and is defined by $$g^{-1}(A) = \{x \in S_1, g(x) \in A\}$$  
If the random variable $Y$ is defined by $Y = g(X)$, then write for any set $A \sub S_2 $ 

$$
\begin{aligned}
 P(Y \in A) &= P(g(X) \in A) \\
 &= P(\{x \in S_1: g(x) \in A\}) \\
 &= P(X \in g^{-1}(A))\ .
\end{aligned}
$$

> Define $\alpha$: $S_1 = {x: f_X(x)> 0}$ and $S_2 = {y:y=g(x) for some x \in S_1}$

**Theorem**: Let $X$ have cdf $F_X(x)$, let Y = g(X), and let $S_1$ and $S_2$ be defined as ($\alpha$).
> a.If $g$ is an increasing function on $S_1$, $F_Y(y) = F_X(g^{-1}(y))$ for $y \in S_2$.
> b.If $g$ is an decreasing function on $S_1$ and $X$ is a continuous random variable, $F_Y(y) =1 - F_X(g^{-1}(y))$ for $y \in S_2$.


---
<h2>Reference</h2>

[Casella, G., Berger, R. L. (2002). Statistical Inference]