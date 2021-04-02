import copy
import time

startTime = time.time()
scoreSet = [
    {
        'list': [3, 2, 1],
        'h': 0
    },
    {
        'list': [3, 2],
        'h': 1
    },
    {
        'list': [3],
        'h': 2
    },
    {
        'list': [3, 1],
        'h': 3
    },
    {
        'list': [],
        'h': 4
    },
    {
        'list': [1],
        'h': 5
    },
    {
        'list': [2],
        'h': 6
    },
    {
        'list': [2, 1],
        'h': 7
    },
]


def possibleStateList(state):
    """
    return ve list state
    """
    result = []
    if len(state[0]) > 0:
        if len(state[1]) == 0 or (len(state[1]) > 0
                                  and state[1][-1] > state[0][-1]):
            tmp = copy.deepcopy(state)
            tmp[1].append(tmp[0][-1])
            tmp[0].pop(-1)
            result.append(tmp)
        if len(state[2]) == 0 or (len(state[2]) > 0
                                  and state[2][-1] > state[0][-1]):
            tmp = copy.deepcopy(state)
            tmp[2].append(tmp[0][-1])
            tmp[0].pop(-1)
            result.append(tmp)

    if len(state[1]) > 0:
        if len(state[0]) == 0 or (len(state[0]) > 0
                                  and state[0][-1] > state[1][-1]):
            tmp = copy.deepcopy(state)
            tmp[0].append(tmp[1][-1])
            tmp[1].pop(-1)
            result.append(tmp)
        if len(state[2]) == 0 or (len(state[2]) > 0
                                  and state[2][-1] > state[1][-1]):
            tmp = copy.deepcopy(state)
            tmp[2].append(tmp[1][-1])
            tmp[1].pop(-1)
            result.append(tmp)

    if len(state[2]) > 0:
        if len(state[0]) == 0 or (len(state[0]) > 0
                                  and state[0][-1] > state[2][-1]):
            tmp = copy.deepcopy(state)
            tmp[0].append(tmp[2][-1])
            tmp[2].pop(-1)
            result.append(tmp)
        if len(state[1]) == 0 or (len(state[1]) > 0
                                  and state[1][-1] > state[2][-1]):
            tmp = copy.deepcopy(state)
            tmp[1].append(tmp[2][-1])
            tmp[2].pop(-1)
            result.append(tmp)

    return result


def calH(state):
    for ss in scoreSet:
        if ss['list'] == state[2]:
            return ss['h']


state = [[3, 2, 1], [], []]
goal = [[], [], [3, 2, 1]]
seen = []
# path = [{'state': state, 'h': calH(state)}]


def findPath(currentState, path):
    if currentState == goal:
        print(path)
        print('Step: {}'.format(len(path) - 1))
        # return currentState
        print('Time execute: {}'.format(time.time() - startTime))
        return
    else:
        stateList = possibleStateList(currentState)
        uniqueList = []
        for state in stateList:
            if state not in seen:
                seen.append(state)
                uniqueList.append(state)

        for state in uniqueList:
            tmp = copy.deepcopy(path)
            tmp.append(state)
            findPath(state, tmp)


findPath(state, [state])