def maximum_importance (S, M, N):
    # Write your code here
    i=1
    max1 = 'a'
    
    for i in range(0,N):
        if S[i-1]>S[i]:
            
            max1 =  S[i]
            #print(max1)
    x = S.index(max1)
    max2 = 'a'
    for i in range(0,N):
        if S[i-1]>S[i]:
            if S[i]== max1:
                continue
            max2 = S[i]
            
    print(max1,max2)
    D = dict({'a':1,'e':5})
    print(D[max1]+D[max2])
    
     
N, M = map(int, input().split())
S = input()

out_ = maximum_importance(S, M, N)
#print (out_)
