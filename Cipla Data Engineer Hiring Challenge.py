def max_value (n, k):
    N = [ i for i in n]
    Q = N
    m = []
    for i in range(len(Q)):
        d = Q.pop(i)
        S = [int(''.join(Q))]
        for j in S:
            m.append(j%k)
            Q.insert(i,d)
            break
    N = int(''.join(N))
    m.append(N%k)
    return max(m)

T = int(input())
for _ in range(T):
    n =input()
    k = int(input())
    out_ = max_value(n, k)
    print( out_)
