import numpy as np
def count():
    A = [(x) for x in input().split()]
    A  = [float(x) for x in A]
    a, b,rel =  [],[],[]
    q,d = 0, 0.2
    for n in np.arange(0,1,.2):
        while(q<5):
            a.append([])
            for i in A:
                if (i>n and i<n+d):
                    a[q].append(i)
            b.append(len(a[q]))
            q+=1
            break
    ln = min(b)
    for k in a:
        for j in range(ln):
            rel.append(k[j])
    return (rel)
count()
