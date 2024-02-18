

# CMPS 2200 Assignment 1

**Name:** Nicolas Labarca


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes, This is because as n approaches infinity, the function 2^n+1 grows at a rate that is asymptotically less than or equal to 2^n.  In big O notation, we are concerned with the behavior of functions for large values of n. Since 2^n+1 is essentially 2 x 2^n, it grows only slightly faster than 2^n, making it a mamber of O(2^n).
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  Yes, for 2^2n to be O(2^n), , there must exist constants c and n0 such that 2^2n =< c * 2^n for all n >= n0. We can rewrite 2^2n as (2^n)^2. After we can divide by both sides by 2^n, which holds true if we choose c >= 1 and any n0, thus making 2^2n indeed O(2^n)
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  If we take the logarithm of both sides, we get log2 n^1.01 = 1.01 *log2 n =< c *log2 n. However, for any constant c, there will be a value of n for which 1.01⋅log 2n > c⋅log 2n holds true. Therefore n^1.01 not equal O(log 2n).
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
.  For n to the power of 1.01 to be in the set Ω(log 2n), there must exist constants where n to the power of 1.01 is greater than or equal to a constant multiple of the logarithm base 2 of n for all sufficiently large values of n. Given that n to the power of 1.01 grows at least as fast as the logarithm base 2 of n for sufficiently large values of n, it is indeed in Ω(log 2n).

  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  For the square root of n to be in O((logn) 3), there must exist constants where the square root of n is less than or equal to a constant multiple of the cube of the logarithm of n for all sufficiently large values of n.Given that the square root of n grows slower than the cube of the logarithm of n for sufficiently large values of n, it is indeed in O((logn) 3).
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  For the square root of n to be in Ω((logn) 3), there must exist constants where the square root of n is greater than or equal to a constant multiple of the cube of the logarithm of n for all sufficiently large values of n. However, as the square root of n grows slower than the cube of the logarithm of n for sufficiently large values of n, it is not in Ω((logn) 3).


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  It begins by checking if the input x is either 0 or 1. In these cases, it returns x itself, as these are the base cases of the Fibonacci sequence where the sequence starts with 0 and 1. If x is greater than 1, the function recursively calls itself with x - 1 and x - 2 to compute the Fibonacci numbers for the preceding two indices. This recursive process continues until the base cases are reached. Finally, it sums up the results of these recursive calls and returns the value, which represents the Fibonacci number at index x. Therefore, the function essentially generates the Fibonacci sequence up to the specified index x
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work and span of the provided iterative, sequential implementation of the longest_run function are both O(n), where n represents the length of the input list mylist. In terms of work, each element in the list is processed once, contributing to a linear increase in the total number of operations performed. Likewise, the span, which represents the length of the critical path, is also proportional to n because each iteration of the loop depends on the previous one. Therefore, as the size of the input list grows, both the work and span of the algorithm increase linearly, making it suitable for analysis in the context of parallelism.
. 
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  The work and span of the provided recursive, divide and conquer implementation of the longest_run_recursive function are both dependent on the size of the input list mylist. In terms of work, the algorithm traverses through each element of the list exactly once during the recursion, performing a constant amount of work at each step. Consequently, the work is O(n), where n represents the length of the input list. As for the span, the algorithm divides the input list into halves recursively, resulting in a binary tree-like structure. The longest path from the root of this recursion tree to a leaf node, which represents the critical path, has a length of O(logn). Therefore, the span of this algorithm is logarithmic in terms of the length of the input list. In summary, the work is linear, while the span is logarithmic.
.  
.  
.  
.  

  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  In this parallelization scheme, where each recursive call spawns a new thread, the work and span of the algorithm are affected. The work remain O(n) since each element of the input list is still visited only once, regardless of parallelization. However, the parallelization alters the span of the computation. With each recursive call spawning two new threads for the left and right halves of the input, the execution forms a binary tree-like structure. As a result, the length of the longest path in this tree, which represents the span, is logarithmic with respect to the size of the input list, denoted as O(logn). Therefore, while the work remains linear, the span decreases due to parallelization, resulting in potentially faster execution times when running on parallel architectures.
.  
.  
.  
