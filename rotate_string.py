"""
 Rotate a given string h by r positions to the left and return the rotated string.
 Input:
  h = "hello", r = 2
  h= "company",r=3
  Output:
 "lohel"
 "anycomp"

h[-r:] gives you the last r characters of the string (which will be moved to the front).

h[:-r] gives you everything from the beginning of the string up to len(h)-r (which will be moved to

 """

string=input("enter the sring:")
k=int(input("enter the rotation:"))
k=k%len(string) #if k len is grater than string 
rotat=string[-k:]+string[:-k]
print(rotat)

"""
Code	Output	Explanation
h[k:]	llo	From index 2 to end (left part after rotate)
h[:k]	he	First 2 characters
h[-k:]	lo	Last 2 characters (right rotation part)
h[:-k]	hel	All except last 2 characters
"""