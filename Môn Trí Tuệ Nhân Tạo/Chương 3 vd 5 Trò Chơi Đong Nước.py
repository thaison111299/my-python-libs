a = 0  # 8
b = 0  # 10
la = 8
lb = 10
c = 6


# l1: a = 8 -> a = 0 
# l2 b = 0  -> b = 10 
# l3 b > 0 and a < 8 -> a += b, b = 0  if a > la => a = la , b = a-la
moves = []
moves.append([0, 0, 0])
while a != c and b != c:
    if a == la:
        a = 0
        moves.append([a, b, 1])
    elif b == 0:
        b = lb
        moves.append([a, b, 2])
    elif a < la and b > 0:
        # do het nuoc tu b sang a
        a += b
        b = 0
        if a > la:
            b = a-la
            a = la
        moves.append([a, b, 3])
        # if(b ==0):
        #   moves.append([a, b)

print(moves)

print('A  B  Luật')
for move in moves:
    print('{}  {}  '.format(move[0], move[1]), move[2])
