a=[1,2,3,4]
b=[3,4,7,8]
ag="abcdef"
bs="cdefg"
c=set(a)&set(b)#common
d=set(a)^set(b)#unique
cg=set(ag)&set(bs)#common
dg=set(ag)^set(bs)#unique
print(c)
print(d)
print(cg)
print(dg)


"""
Set operations allow efficient handling of unique elements. Key operations include:

Union (|) – Combines all elements from both sets.

python
Copy
Edit
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5}
Intersection (&) – Finds common elements.

python
Copy
Edit
print(set1 & set2)  # {3}
Difference (-) – Finds elements in one set but not in the other.

python
Copy
Edit
print(set1 - set2)  # {1, 2}
Symmetric Difference (^) – Finds unique elements in both sets.

python
Copy
Edit
print(set1 ^ set2)  # {1, 2, 4, 5}
"""