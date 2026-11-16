#Create a set from {'apple', 'banana', 'orange', 'apple', 'pear'} and print it, and list [1, 2, 2, 3, 3, 3] using set() and print it.

fruit = {'apple', 'banana', 'orange', 'apple', 'pear'}
print(fruit)

l = [1,2,2,3,3,3]

l = set(l)
print(l)

#Take s = set([1, 2, 3, 4, 5]). Use add() to add 6, then add 3 again. Print the set after each step.

s = set([1,2,3,4,5])

s.add(6)
print(s)
s.add(3)
print(s)

#Given s = {1, 2, 3, 4, 5} and t = {6, 7, 8} use update() 
s = {1,2,3,4,5}
t = {6,7,8}

s.update(t)
print(s)

s.update()

#For s = {1, 2, 3, 4, 5}, remove 3 using remove(), then try discard(3) again

s = {1,2,3,4,5}
s.remove(3)
print(s)
s.discard(2)
print(s)

#Union

s = {1, 2, 3, 4, 5}
t = {4, 5, 6, 7, 8}

s.union(t)
print(s)

#Intersection and intersection_update()

s = {1, 2, 3, 4, 5}
t = {4, 5, 6, 7, 8}

print(s.intersection(t))

s = {1, 2, 10, 12}
t = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s.intersection_update(t)
print(s)