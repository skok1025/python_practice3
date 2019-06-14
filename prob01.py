subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

def returnline(*l):
    results = []
    for s in l: results.append(s[0])
    else: results.append("\n")
    for s in l: results.append(s[1])
    else: results.append("\n")
    return results


for str in returnline(subs,verbs,objs):
    print(str,end=' ')
