s1 = "A aaaa bb c"
s2 = "& aaa bbb c d"

d1 = {}
d2 = {}

def alpha_count(s):
    d = {}
    for e in s:
        if e.isalpha() and e.islower():
            if e in d:
                d[e] = d[e] + 1
            else:
                d[e] = 1
    return d

def print_data(d):
    s = ''
    for e in d:
        if s != '':
            s = s + ', '
        s = s + str(d[e]) + " '" + e + "'"
    return s

print("s1 has ", print_data(alpha_count(s1)))
print("s2 has ", print_data(alpha_count(s2)))