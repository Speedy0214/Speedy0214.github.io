---
layout: post
title: "abstract data type(ADT)"
categories: [Algorithm]
date: 2019-07-16
---

### ADT(abstract data type)
> a DATA TYPE is a set of values and a set of operations on those values.
> an *abstract data type* is a data type whose representation is hidden from the client. When using an ADT, we focus on the operations specified in the API and pay no attention to the data representation; when *implementing* an ADT, we focus on the data, then implement operations on that data.

> Abstract data type are important because they support encapsulation in program design.
>> - Precisely specify problems in the form of APIs for use by diverse clients
> - Describe algorithms and data structures as API implementations

>**Using abstract data types.**  we begin by describing how to write programs that use a simple data type named Counter whose values are a name and a nonnegative integer and whose operations are create and initialize to zero, increment by one, and examine the current value.To use a Counter, you need to learn our mechanism for specifying the operations defined in the data type and the Java language mechanisms for creating and manipulating data-type values  
>> **API for ADT.** To specify the behavior of an ADT, we use *(API)*, which is a list of *constructors* and *instance methods*, description in this API for Counter:  

>> ![API for Counter](/assets/Algorithm/api_counter.jpg)


>> **Inherited methods.** Various Java conventions enable a data type to take advantage of builtin language mechanisms by including specific methods in the API. For example, all Java data types inherit a toString() method that returns a String representation of the datatype values. Java calls this method when any data-type value is to be concatenated with a String value with the + operator

>> **Pass by value and pass by reference.**

**implementing an ADT**
>> **Instance variables**
>> **Constructors**
>> ![Counter implement](/assets/Algorithm/Counter.jpg)
[Counter](/assets/code/Algorithm/Counter.java)


### API, clients, and implementations
>- Specify an API. The purpose of the API is to separate clients from implementa- tions, to enable modular programming. We have two goals when specifying an API. First, we want to enable clear and correct client code. Indeed, it is a good idea to write some client code before finalizing the API to gain confidence that the specified data-type operations are the ones that clients need. Second, we want to be able to implement the operations. There is no point specifying opera- tions that we have no idea how to implement.
> - Implement a Java class that meets the API specifications. First we choose the instance variables, then we write constructors and the instance methods.
>- Develop multiple test clients, to validate the design decisions made in the first two steps.

>>![An abstract data type for a simple counter](/assets/Algorithm/An abstract data type for a simple counter.jpg)

### Bags, Queues, and Stacks
![BAGS, QUEUES, AND STACKS](/assets/Algorithm/Algorithm_bag_queue_stack.jpg)

























---


---
<h2>Reference</h2>

<small>[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/)</small>
