import re
A =input()
A = re.sub(r"[-()\"#/@;:<>{}`+=~' ''|.!?,]", "", A)
A = [x for x in str(A)]
B = [[str(x)] for x in input().split()]
o,arr =0, []
for i in B:
    while(o<len(B)):
        arr.append([])
        for j in range(len(i)):
            for k in range(len(i[j])):
                for l in range(len(A)):
                    if i[j][k]==A[l]:
                        arr[o].append(A[l])
                        break
        o += 1
        break
final = []        
for ok in range(len(arr)):
    final.append([''.join(arr[ok])])
count = 0
for i in B:
    for k in final:
        if i == k:
            count += 1
            print(i)
print(count)
