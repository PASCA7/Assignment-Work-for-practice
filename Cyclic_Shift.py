def cyclic_shift(N,K):
    A = input()
    wer = []
    count = 0
    prev = 0
    B=A[N-1] + A[:N-1]
    print()

    while(1):
        A = A[1:N]+A[0]
        count += 1
            
        if B == A:
            prev += 1
            wer.append(count) 
            count = 0
            
            if prev==K:
                break
                
    return sum(wer)


T = int(input(""))
for t in range(T):    
    N , K  = map(int,input().split())
    print(cyclic_shift(N,K))
    
    
 # https://www.hackerearth.com/practice/codemonk/

