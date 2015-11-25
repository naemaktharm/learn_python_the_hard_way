#!/usr/bin/env python

"""
Insertion sort in ascending order
"""

import sys

# A is the array to sort
def insertionSort(A):
    print "\nOrdering..."
    for j in range (1,len(A)):
        print "-------- "
        print "\tkey= A[j]=",A[j]
        print "\ti= j-1 =",str(j-1)
        key=A[j];
        i=j-1;
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            print "\t", A, "##",
            print "i:",i,
            print "#",
            print "j:",j,
            print "#",
            print "key:",key
            i-=1
        print "\tExchange A[i+1]=",str(A[i+1]),"with",str(key)
        A[i+1]=key    
    print "--------";
    return A

###################################
    
if len(sys.argv)<=1:
    print "\nUsage: " + sys.argv[0] + " ([0-9]+ )+"
    print "\nExample: " + sys.argv[0] + "1 2 3 99 1000"
    exit(1);    

n=len(sys.argv)-1 #number of elements to sort

print "You want to order " + str(n) + " elements"
print "The initial list is: \nA: ",

A=[]
for elems in sys.argv[1:]:
    #A.insert(int(elems),i);
    A.append(int(elems))
    
print A;

B=insertionSort(A)

print "\nOrdered list is: \nA: ",
print B
    
print "\n"