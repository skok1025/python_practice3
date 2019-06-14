def frange(val, basic=0.0, step=0.1):
    l = []
    if val < basic:
        start = val
        stop = basic
    else:
        start = basic
        stop = val

    for num in range(int(start*10),int(stop*10),int(step*10)):
        l.append(num/10)
    return l

print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))



