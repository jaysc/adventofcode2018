# Day 8

Really like today's challenge. Took me a while to understand the question itself as I couldn't tell what the numbers meant. After I figured it out, I could tell this was a another recursion question, and you could easily (although may not be obvious) see how the recursion would be set up.

Major problem I ran into was the use of a global counter during the recursion. I didn't realise the counter would revert back to its upper level value. Solution was to create a class counter and use that.