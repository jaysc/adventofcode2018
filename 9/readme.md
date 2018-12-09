# Day 9

Part 1 and Part 2 are in the same files.

This one took a while to understand what was going on, but then the coding wasn't that difficult.

However, I did attempt this using pointers and inserting at index. While part 1 was easy to do, part 2 took way too long to compute.
After reading the reddit, I found out inserts are very performance heavy. Instead, Deque is used along with its rotation code.
With that, I rotate the list so that the first entry is always the current.