
def allPossibleSum(a):
    b = [0]*len(a)
    b[0] = a[0]

    
    for i in range(1, len(a)):
        b[i] = (  a[i]+b[i-1]  )

    
    k = len(b)  #k = 5 
    for i in range(k-1, 0, -1): #4 - 1
        # print(i)
        c = len(b)#c = 5  o vong lap dau tien
        sub = b[c-i-1]  #5 - 4 - 1  = 0
       
        for j in range(i,0, -1):#lap: 4 3 2 1, gia tri 4 3 2 1 luon 
            b.append(  b[c-j]  - sub)

            # c - j = 5 - 4 = 1, j = 4 o vong lap dau tien
            # print(c-j)
    
    # b = [z%m for z in b]
    print(b)


allPossibleSum([1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,10, 1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])

