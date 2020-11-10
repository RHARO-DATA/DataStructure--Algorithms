"""
Given an Integer, find the number of 1 bits it has

"""

def one_bits(num):
    count = 0
    while num > 0:
        if num & 1  ==1 :
            count +=1
        num = num >> 1
    return count

print(one_bits(23))
