t1 = ('a','b',21)
t2 = ('b','a',21)

a = []
a.append(t2)
if t1 not in a:
    a.append(t1)
print(a)