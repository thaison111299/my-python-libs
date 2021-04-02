

board = [
    [4, 6], [7, 4], [5, 3], [8, 7], [3, 4]
]

idx = 1
for b in board:
    b.insert(0, idx)
    idx += 1
# print(board)
# tt a b
# 1 column of board in  a work

smallGroup = [work for work in board if work[1] <= work[2]]
bigGroup = [work for work in board if work[1] > work[2]]


def sortA(val):
    return val[1]


def sortB(val):
    return val[2]


smallGroup.sort(key=sortA)
bigGroup.sort(key=sortB, reverse=True)

print(smallGroup)  # 1 5
print(bigGroup)  # 2 3 4

order = []
order.extend(smallGroup)
order.extend(bigGroup)

print('Thứ Tự Công Việc Gia Công 2 Máy Tối Ưu Là: ')
for i, o in enumerate(order):
    if i != len(order) - 1:
        print('D{}, '.format(o[0]), end='')
    else:
        print('D{}'.format(o[0]), end='')
