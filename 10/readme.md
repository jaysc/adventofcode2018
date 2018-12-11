# Day 10

Part 1 and 2 are in the same file

1st hint was the usage of checking if the border changes after the next iteration. It seems like a weak assumption but appears to work fine. Most likely the question was first created via making the positions then applying random velocity values.

So the inital attempt was using classes. As expected, with the real input it took too long to compute.
After looking online for hints, I found the usage of the `Map` function and `finall` which is much nicer. 
I then noticed how people used `i*vs` to workout the values. Finally, removing the class usage and using only the list speeds up everything

Overall, was fun to do.
