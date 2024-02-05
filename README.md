# Structify Take-Home Question

## Problem Statement
This README attempts to answer the following question: given a list of chords, count the number of intersections, if any. This document outlines the mathematical proof and the algorithmic approach to solving this problem. 

Args: 
    rad (list) = radian measure of start or end of the chord
    point (list) = identifiers of the chord

Output: 
    int = number of intersections

## Solution Approach

An inversion is defined within a sequence S = [a1, a2, ..., an], and a reference sequence R = [r1, r2, ..., rn] containing the same elements, as a pair of indicies (i, j), such that i<j and the corresponding elements ai, aj in S are out or order with respect to their position in R. 

### Initial Preparation
We first perform an initial sorting of rad such that s1 < s2 < ... < sn, and that for each chord, si < ei. Let this be S1. Then, let S2 be the sequence with only the endpoints according to S1. 

### Reference Sequences
We introduce 2 reference sequences. R1 = [s1, e1, s2, e2, ..., sn, en], and R2 = [e1, e2, ..., en]. Let I1 be the number of inversions in the list S1 with respect to R1, and I2 be the number of inversions in the list S2 with respect to R2. 

### Proof
Now, we show that the number of intersections is I = I1 - 2I2. Consider 2 segments with points (s1, e1) and (s2, e2). We break down the interations with 3 cases. 

Case 1: s1 < e1 < s2 < e2.
I1 = 0, I2 = 0. 
I = I1 - 2I2 = 0 Intersection

Case 2: s1 < s2 < e1 < e2 
I1 = 1, I2 = 0. 
I = I1 - 2I2 = 1 Intersection

Case 3: s1 < s2 < e2 < e1
I1 = 2, I2 = 1. 
I = I1 - 2I2 = 0 Intersection


From the case analysis above, we see that each intersection controbute to one inversion in I1. In case 3, no inversion is observed but there's I1 = 2 and I2 = 1. So I = I1-2I2, the inversions from non-intersecting chords are cancelled out, which leaves only inversions corresponding bto actual intersections. 

### Final Notes
