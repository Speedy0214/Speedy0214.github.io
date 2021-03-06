---
layout: post
title: "Probability Basic"
categories: [Machine Learning]
date: 2019-06-06
---

## Probability
---

### Exercise  

>1.$X, Y$ are random variables , $P$ is the probability distribution.  Write the relation between $P(X), P(X,Y), P(Y \| X)$  

>2.$X, Y$ are discrete random variables,$Y \in [y_1,\cdots, y_n],$ $P$ is the probability. Write the relation between$P(X), P(X,Y)$  

>3.$X$ is real-valued continuous random variable, $p(x)$ is the probability density of $X = x$, Write the probability of $x\in(a, b)$ and $x\in(-\infty, +\infty)$  

>4.$X$ is real-valued continuous random variable, $p(x)$ is the probability density of $X = x$, Write $E(x)$(the expectation of $x$) and $var(x)$(The variance of $x$)  

>5.Sample $(X,Y) = \lbrace (x_1, y_1), \cdots,(x_n, y_n),\cdots, (x_N, y_N) \rbrace $,consider the sum-of-squares error function given by  

$$E(\boldsymbol w)= \frac{1}{2}\sum_{n=1}^{N}[h(x_n, \boldsymbol w) - y_n]^2$$

>>in which the function $h(x,\boldsymbol w)$ is given by the polynomial  

$$h(x, \boldsymbol w) = w_0+w_1x+w_2x^2+...+w_Mx^M = \sum_{j=0}^{M}w_jx^j$$  

>>Show that the coefficients $\boldsymbol w = \lbrace w_i \rbrace$ that minimize this error function are given by the solution to the following set of linear equations  

$$\sum_{j=0}^{M}A_{ij}{w_j} = Y_i$$  

>> where  

$$A_{ij} = \sum_{n=1}^{N}(x_n)^{i+j}, Y_i = \sum_{n=1}^{N}(x_n)^iy_n$$



---

## Bayesian probabilities





---
<h2>Reference</h2>

<small>Pattern Recognition and Machine Learning BISHOP Chapter1.1</small>
