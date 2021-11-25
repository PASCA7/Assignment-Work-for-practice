def maxBeauty (N, A):
    # Write your code here
    arr=[]
    for i in range(len(A)-1,-1,-1):
        j=0
        while(j<len(A)):
            if j>len(A):
                break
             asd = []
             for k in range(j,i+1):
                 asd.append(A[k])
             j+=1
             arr.append(asd)
    arr=[x for x in arr if x!= []]
    res=[]
    for i in arr:
        d=0
        for j in range(len(i)):
            d=i[j]+d
        res.append(d*max(i))
    print(max(res))
    
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    out_ = maxBeauty(N, A)
    print (out_)
