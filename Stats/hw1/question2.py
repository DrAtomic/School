omega = {'a','b','c','d','e','f','g'}
A = {'a','b','c','d'}
B = {'a','b','f','g'}
C = {'d','e','f','g'}


def union(A,B):
    return (A | B)

def intersection(A,B):
    return(A & B)

def compliment(A):
    global omega
    return omega - A



print(intersection(union(A,B),C))
print(union(compliment(intersection(A,B)),C))
print(union(intersection(A,union(B,C)),intersection(A,(compliment(union(B,C))))))
print(intersection(intersection(compliment(A), compliment(B)),compliment(C)))
