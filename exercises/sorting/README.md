# Sorted Stream

## Context

The [Fibonacci](../fibonacci/README.md) exercise introduced you to the concept of generators. This exercise will continue on that path to become more comfortable with the concept of streams.

## Objective

This exercise is meant to challenge your grasp on how streams differ from in-memory data types like `list`. Both lists and generators are iterable (i.e. you can iterate over them with a `for` loop), but only lists allow access at specific indices (e.g. `my_list[0]`). Because a stream is potentially never-ending, such as in the case of a Kafka topic, we must consume the stream to access further elements.

In this exercise we will implement a function `sorted_stream` which will take as an argument some arbitrary number of streams. These streams are sorted ascendingly within themselves, but there is no guaranteed ordering between streams. For example, Stream 1 may contain [1, 3, 5] while Stream 2 contains [2, 4, 6], but no stream will contain something like [5, 2, 8, 6...]. Your task is to combine these streams into a single ordered stream. Your solution should be implemented as a generator. Following on the previous example, if given Stream 1 and Stream 2, your function should generate [1, 2, 3, 4, 5, 6].

## Hints

You will not find a solution to this online.

`def func(*args)` means that `args` will be a list that can contain any number of entries.

`next(stream)` is a convenient way to retrieve the next item in a stream without using a `for` loop.

`next` will raise `StopIteration` when it reaches the end of an iterator.

There will be unit tests that won't pass if you try to consume streams as a list and order them in memory.