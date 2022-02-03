d={'a':12,'b':25,'c':84,'d':52}
high=max(d.values())
print(high)
for i in d.keys():
    if d[i]==high:
        print(i)
