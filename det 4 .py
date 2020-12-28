
# print(a)


test = [[2,2,3], [3,3,6], [32,12, 9]]
def det3(a):
    b = 0
    for  i in range(3):
        # a[0][i]*a[0][i]*a[0][i]      #00, 01, 02
        c = 1  
        for j in range(3):
            c *= a[0+j][(i+j)%3]
        b += c 
    

    d = 0
    for i in range(2, -1, -1): # 2 - 0
        # a[0][i]*a[0][i]*a[0][i]      #02, 01, 00
        e = 1
        for j in range(0, 3):
            e *= a[j][(i-j) % 3]
        d += e 
    return b - d 
    
# det3(test)


a = [[1, 0, 4, -6], [2, 5, 0, 3], [-1, 2, 3, 5], [2, 1, -2, 3]]
def det4(a):

    # b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    b = []
    # for i in range(4):
        #00 01 02 03
    c = 0 

    x = 0 #am hay duong  
    for i in range(4):
        #4 lan duyet qua ca ma tran 
        #mac dinh hang 0 bi bo
        for j in range(4):
            for k in range(4):
                if j != 0 and k != i:
                    b.append(a[j][k])
        
                # print(a[j][k], end = " ") 
            # print()
        # chuyen thanh 3x3
        b = [b[0: 3],b[3:6],b[6:9]]
        if(x%2 == 0):
            c+= a[0][i]*det3(b)
        else:
            c -= a[0][i]*det3(b) 
        # print("\n\n\n\n")
        b = []
        x+=1 
    # return c 
    # print(c)
    return c
# det4(a) 

print(det4([[2,2,1,0], [-3,1,2,1],[0,4,-3, 0],[5,0,4,-2]]))