---
layout: post
title: "introduce to Graph"
categories: [Graph]
date: 2019-07-12
---
In graph theory, a graph is a structure amounting to a set of objects in which some pairs of the objects are in some sense "related". The objects correspond to mathematical abstractions called vertices (also called nodes or points) and each of the related pairs of vertices is called an edge (also called link or line).Typically, a graph is depicted in diagrammatic form as a set of dots or circles for the vertices, joined by lines or curves for the edges. Graphs are one of the objects of study in discrete mathematics


##### Graph
A graph is a pair $G = (V, E)$, where $V$ is a set whose elements are called *vertices*(singular: vertex), and $E$ is a set of two-sets of vertices, whose elements called edages.  

The vertices $x$ and $y$ of an edage {$x, y$} are called the *endpoint*. The edge is said to *join* $x$ and $y$ and to be *incident* on $x$ and $y$. A vertex may not belong to any edge.

A multigraph is generalization that allows multiple edges adjacent to the same pair of vertices, In some texts, multigraphs are simple called graphs.

Sometimes, graphs are allowed to contain loops, which are edges that join a vertex to itself. For allowing loops, the above definition must be changed by defining edges as multisets of two vertices instead of two-set.  

The *order* of a graph is its number of vertices $V$. The *size* of a graph is its number of edages $E$. However, in some context, such that for expressing the computational complexity of algorithms, the size of $V+E$. The *degree* or *valency* of a vertex is the number of edages that are incident to it; for graphs with loops, a loop is counted twice.  

In a graph of order $n$, the maximum degree of each vertex is n − 1 (or n + 1 if loops are allowed), and the maximum number of edges is $n(n − 1)/2$ (or $n(n + 1)/2$ if loops are allowed).  

The edges of a graph define a symmetric relation on the vertices, called the adjacency relation. Specifically, two vertices x and y are adjacent if {$x, y$} is an edge.

















---


---

<h2>Reference</h2>

<small>[wiki/Graph_(discrete_mathematics)](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))</small>
