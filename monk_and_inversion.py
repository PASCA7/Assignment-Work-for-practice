count = 0
for i in range(N):
    
    for p in range(N):
        
        if i<= p:
            
            for j in range(N):
                
                for q in range(N):
                    
                    if j<=q:
                        if M[i][j] > M[p][q]:
                            print(M[i][j],M[p][q])
                            count += 1
print(count)
