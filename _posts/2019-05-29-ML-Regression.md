---
layout: post
title: "Regression"
categories: [Machine Learning]
date: 2019-05-29
---

## [Regression](/assets/Regression.pdf)

---

<h3>LinearRegression</h3>

- [sklean ref](https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares)

- [Reference Implementation](http://localhost:8888/notebooks/LR.ipynb)  


### step 1 :Hypothesis  

$$h_w(x) = w_{0}1+w_{1}x_1+...+w_nx_n = XW$$


$$X = \begin{bmatrix}
x_{11}  \cdots x_{1n} \\
\vdots \ddots\ \vdots \\
x_{m1}  \cdots x_{mn} \\
 \end{bmatrix},
 W = \begin{bmatrix}
 w_{1} \\
 \vdots \\
 w_{n}
  \end{bmatrix},
  Y = \begin{bmatrix}
  y_{1} \\
  \vdots \\
  y_{m}
   \end{bmatrix},
 \\ m = samplesize, n = featuresize$$

### step 2 : Evaluate Function
*define Loss Function*  

$$
L(w) = \frac{1}{2m}\sum_{i=1}^m (h_{w}(x^i) -y^i)^2
$$

In Matrix Form  

$$
L(W) = \frac{1}{2}(XW-Y)^T(XW-Y)
$$

### step 3 : find a suitable w

*gradient*  *for every j*  

$$ \frac{\partial L(w)}{\partial w_j} = \frac{1}{m}\sum_{i=1}^{m}[h_w(x^{i}) -y^{i}]x_j$$  

In matrix form

$$\frac{\partial L(W)}{\partial W} = X^T(XW−Y)$$

*use gradient decent*

*for every j repeat unitl converge*  

$$w_j = w_j -\alpha\frac{\partial L(w)}{\partial w_j}$$  

In matrix form  

$$W = W -\alpha X^T(XW−Y)$$

```python

class LinearRegression(object):
    def __init__(self, ):
        pass


    def fit(self, X, y):
        """
          while not converge:
            w = w - alpha*grad
        """
        pass


    def loss(self, w, X, y):
        pass

    def _grad(self, w, X, y):
        pass

    def predict(self, X):
        pass
```










---
<h2>Reference</h2>

<small>[speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2017/Lecture/Regression.pdf](http://speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2017/Lecture/Regression.pdf)</small>
