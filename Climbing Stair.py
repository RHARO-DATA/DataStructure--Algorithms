"""
Climbing stair

You are climbing a stair case. it takes n steps to reach to the top

each time you can either climb 1 or 2 steps, in how many distinct ways can you climb to the top?
Given n will be a positive integer

Ex.
input: 2
Output: 2

"""
# Solution Fibonacci
def climb_stair(self,n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in ranges(3, n + 1):
        third = second + first
        first = second
        second = third
    return second

# solution Recurtion

class sol:
    def rec_sol(self, n: int) ->:
        if n == 0:
            return 1
        if n == 1:
            return 1
        return self.rec_sol(n-1) + self.rec_sol(n-2)