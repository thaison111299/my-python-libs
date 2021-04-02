import copy
from typing import Match


startList = [[1, 0, 7], [5, 4, 8], [2, 3, 6]]
endList = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]
currentPos = 0

seen = []


def allMoves(arr):
    result = []
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                t = copy.deepcopy(arr)
                if i+1 <= 2:
                    t[i][j], t[i+1][j] = t[i+1][j], t[i][j]
                    result.append(t)
                    t = copy.deepcopy(arr)
                    # print('t:', t)
                if i-1 >= 0:
                    t[i][j], t[i-1][j] = t[i-1][j], t[i][j]
                    result.append(t)
                    t = copy.deepcopy(arr)
                    # print('t:', t)

                if j+1 <= 2:
                    t[i][j], t[i][j+1] = t[i][j+1], t[i][j]
                    result.append(t)
                    t = copy.deepcopy(arr)
                    # print('t:', t)

                if j-1 >= 0:
                    t[i][j], t[i][j-1] = t[i][j-1], t[i][j]
                    result.append(t)
                    t = copy.deepcopy(arr)
                    # print('t:', t)
                break
    return result


def calH(cur_lis):
    res = 0
    for i in range(3):
        for j in range(3):
            if cur_lis[i][j] != 0 and cur_lis[i][j] != endList[i][j]:
                res += 1

    return res


def findPath(currentList, result):
    global currentPos
    if(currentList == endList):
        return result
    else:
        allPossibleMoves = allMoves(currentList)
        smallestH = 999
        smallHMoves = []
        for move in allPossibleMoves:
            smallestH = min(smallestH, calH(move))
        for move in allPossibleMoves:
            currentPos += 1
            if calH(move) == smallestH:
                if(move not in seen):
                    seen.append(move)
                    smallHMoves.append(
                        {'value': move, 'h': calH(move), 'pos': currentPos})
        # co list cac small move
        # tien hanh move cac small move do

        for move in smallHMoves:
            result.append(move)
            anSet = findPath(move['value'], result)

            if(isinstance(anSet, list)):
                print('Kết quả: {} bước'.format(len(anSet)-1))
                # print(anSet)
                for sett in anSet:
                    thutu = sett['pos']
                    print('Thứ tự: s{}'.format(thutu))
                    for row in sett['value']:
                        print(row)
                        # print('\n')
                    print('\n')
                # print(seen)
            # else:
                # print(anSet)

            break
            # print(move['value'])
        return


findPath(startList, [{'value': startList, 'h': calH(startList), 'pos': 0}])
