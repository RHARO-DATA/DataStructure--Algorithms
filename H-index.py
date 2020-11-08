"""
the H-index is a metric that attemps to ensure the productivity and citation impact of the
publication of a scholar. the definition og the h-index is if a scholar has at leasth of their
papers cited h times

given the list of publications of the number of citations a scholar has, find theirh-index.

Example
input :[3,5,0,1,3]
output[3]
explanation: there are 3 publication with 3 or more citations, hence the h-index is 3



"""

def hIndex(publications):
    n = len(publications)
    citations = [0]* (n+1)

    for pub in publications:
        if pub < n:
            citations[pub] += 1
        else:
            citations[n] += 1
    total = 0 
    i = n
    while i >= 0:
        total += citations[i]
        if total >= i:
            return i
        i -= 1
    return i


print(hIndex([5,3,3,1,0]))