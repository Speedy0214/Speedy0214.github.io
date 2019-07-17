---
layout: post
title: "DATA ABSTRACTION"
categories: [Algorithm]
date: 2019-07-17
---

### ADT(abstract data type)
>> a DATA TYPE is a set of values and a set of operations on those values.
>> an *abstract data type* is a data type whose representation is hidden from the client. When using an ADT, we focus on the operations specified in the API and pay no attention to the data representation; when *implementing* an ADT, we focus on the data, then implement operations on that data.

>> Abstract data type are important because they support encapsulation in program design.
>> - Precisely specify problems in the form of APIs for use by diverse clients
>> - Describe algorithms and data structures as API implementations

**Using abstract data types.**  we begin by describing how to write programs that use a simple data type named Counter whose values are a name and a nonnegative integer and whose operations are create and initialize to zero, increment by one, and examine the current value.To use a Counter, you need to learn our mechanism for specifying the operations defined in the data type and the Java language mechanisms for creating and manipulating data-type values  
>> **APIforanabstractdatatype.** To specify the behavior of an ADT, we use *(API)*, which is a list of *constructors* and *instance methods*, description in this API for Counter:  

```java
public class Counter

         Counter(String id)  //create a counter named id
    void increment()         // increment the counter by one
     int tally()             // number of increment since creation
  String toString()          // string representation
```


>> **Inherited methods.** Various Java conventions enable a data type to take advantage of builtin language mechanisms by including specific methods in the API. For example, all Java data types inherit a toString() method that returns a String representation of the datatype values. Java calls this method when any data-type value is to be concatenated with a String value with the + operator



### Bags, Queues, and Stacks
![BAGS, QUEUES, AND STACKS](Algorithm/Algorithm_bag_queue_stack.jpg)










<h2>Reference</h2>

<small>[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/)</small>
















---


---

<h2>Reference</h2>

<small>[wiki/Graph_(discrete_mathematics)](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))</small>
