"""
Optimized List Sum

Create a class that initializes with a list of numbers and has one method called sum. sum should
take in two parameters, star_idx and end_idx and return the sum of the two list from
start_idx(inclusive) to end_idx(exclusive)

Should optmized for the sum method

"""

class ListFastSum:
    def __init__(self, nums):
        self.nums = nums
        self.sum_up_to = []

        curr_sum = 0

        for num in nums:
            curr_sum += num
            self.sum_up_to.append(curr_sum)
        
        self.sum_up_to.append(0)

    def sum(self, star_idx, end_idx):
        return self.sum_up_to[end_idx - 1] - self.sum_up_to[star_idx -1]


print(ListFastSum([1,2,3,4,5,6,7]).sum(2,5))   # 12
print(ListFastSum([1,2,3,4,5,6,7]).sum(0,5)) 


