S = list(input())
l = []
u = []
o = []
e = []
for s in S:
    if s.islower():
        l.append(s)
    elif s.isupper():
        u.append(s)
    elif s.isdigit and int(s)%2 != 0 :
        o.append(s)
    else:
        e.append(s)

final = sorted(l) + sorted(u) + sorted(o) + sorted(e)
print("".join(final))

