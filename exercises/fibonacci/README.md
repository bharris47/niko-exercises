# Fibonacci Sequence

## Context

The [Fibonacci Sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) is a series of numbers where each number is the sum of the two previous numbers. It starts with 0, 1. For example, the first few digits of the fibonacci sequence are 0, 1, 1, 2, 3, 5, 8...

## Objective

This exercise is an introduction to generators which are an important Python concept that can help you write more efficient programs. A generator function is an iterable (i.e. you can iterate over it in a for loop) that lazily produces the next item in the sequence. Common generators you already use may include file objects, or the use of the `range` function.

There is a module in the `fibonacci` package named fib.py with an empty `generate_fibonacci` method signature. Your job is to implement this generator function to provide the correct Fibonacci sequence up to the provided length and make the tests pass.

The use of generators is important to this exercise due to memory constraints. Storing the Fibonacci sequence up to 10 digits in memory is fine, but what if I wanted 4 billion digits? Generators allow us to achieve that with the use of constant memory.

## Hints

`yield` makes a generator a generator. Generators do not use `return`.

There will be dozens of implementations of Fibonacci generators on Google, try to avoid using them.

The Fibonacci Sequence will always start with 0, 1. It is OK to hard code these values at the start of your algorithm.

