# Repeating Pattern Recognizer
## Use
```
i = 0
z = 1
n = [1,2,3,4,5,1,2,3,4,5]
print(rp(n, i, z))
```
In the above code, i is our starting point (0 and 1 for the first number and second number in the list)
With the 1st and 2nd numbers, we check if the 2nd and 3rd match them. If not, we increase z by 1, so we check the first 3 numbers instead.
n is our list. This is where our pattern is.

## Why
I'm making a rock paper scissors game where the AI looks back at your patterns and predicts your next choice based on them.
