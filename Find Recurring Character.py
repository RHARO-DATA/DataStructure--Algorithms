"""
First Recurring Character

Given a String, return the first recurring letter that appears, if there are no recurring letters
return none
Ex.

input: Qwertty  
output: t

"""
def first_recurring(s):
    seen = set()

    for c in s:
        if c in seen:
            return c
        seen.add(c)
    return None


print(first_recurring('qqwertty'))

print(first_recurring('qwerty'))