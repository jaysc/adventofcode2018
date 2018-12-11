# Day 11

This one was a personal failure in terms on figuring out the best way to handle it.

I was able to create a grid with function to work out the values at each coorindates, however finding the best `3x3` square was difficult to figure out.

After giving up a looking for hints on the subreddit, I found someone using `numpy`. This led to the code I have written now with some minor tweaks. That said, I spent a large amount of time examining and figuring out exactly what it was doing.

The `fromfunction` seems self-explanatory, passing in a function as the first argument and applying it to each coordinates.

The next part is the trickiest, understanding what the `sum([grid[x:,y:]] for x for y)` part is doing. For this I examined what it looks like for a `4x4` grid.

```
0 1 2 3
1 2 3 4
2 3 4 5
3 4 5 6
```

Here's a grid with a `function(x,y) return x + y` applied.

First, lets examine this part: `[x:(l+x-w),y:(l+y-w)] for x in range(w) for y in range(w)` where `w=3` and l is the length of the grid + 1 so `l=5`. Here that means x is going `0,1,2` meaning a loop would produce `[0:2],[1:3]`. `y` would be the same, producing two slices.

In turn that actually creates 9 arrays:

```
[0,1] | [1,2] | [2,3] | [1,2] | [2,3] | [3,4] | [2,3] | [3,4] | [4,5]
[1,2] | [2,3] | [3,4] | [2,3] | [3,4] | [4,5] | [3,4] | [4,5] | [5,6]
```

This may not be obvious, but for the first 3 arrays, the first one is the top left 4, then the 2nd one is the middle 4, followed by the top right 4.:
```
0 1 # 1 2 # 2 3
1 2 # 2 3 # 3 4
```
So we can see that there is an overlap on the middle 4.

The next 3 moves down one:

```
1 2 # 2 3 # 3 4
2 3 # 3 4 # 4 5
```
and the last 3 again moves down.

Okay, so now we need to `sum([])` this up, and this is the clever part.
For each array, lets take the top left value. After every 3, we'll write it to the next line:

```
0 1 2
1 2 3
2 3 4
```

This is actually the `3x3` for the top left quadrant! The reason being is that every 3 values, we shifted down the y axis. Summing these values produces the sum of the top left `3x3`.

Another example is the bottom left part of the arrays:

```
1 2 3
2 3 4
3 4 5
```

Again, this is the bottom left `3x3` of the grid.

Essentially, that's what this `sum` is doing, and in doing so produces an array of `3x3` grids. The output looks like this:

```
18 27
27 36
```

Thus we can find the maximum of the summation, find the array location on the summing grid,then we know where the top left coordinate will be.

Expanding this to larger grids will produce the same methods. In a `5x5` grid, instead of `2x2` arrays, there was be `3x3`. Summing them again will count as summing all the `3x3` square arrays on the grid.

---

For part 2, we just record the max value and coordinates for each `w`. As we expand, we see that `w` goes towards < 0 . We can break out the loop then and find the maximum value, w, and the location.