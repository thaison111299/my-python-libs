def get_center(a, i, j):
    return sorted([
        a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i][j - 1], a[i][j],
        a[i][j + 1], a[i + 1][j - 1], a[i + 1][j], a[i + 1][j + 1]
    ])[4]

def get_avr(a, i, j):
    lt = [
        a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1], a[i][j - 1], a[i][j], a[i][j + 1], a[i + 1][j - 1], a[i + 1][j], a[i + 1][j + 1]]
    # print(lt)
    return sum(lt) // 9


a = [[1, 2, 3, 2], [4, 8, 7, 1], [4, 7, 4, 1], [2, 1, 2, 1]]
alpha = 2
center = [1, 1]
# 11 12 13 21 22 23 31 32 33
for i in range(1, len(a) - 1):
    for j in range(1, len(a[i]) - 1):

        i_p = a[i][j]  #diem o giua ma tran
        m_p = get_avr(a, i, j)
        # print('mp: ', m_p)
        if abs(i_p - m_p) > alpha:
            # print('yes')
            a[i][j] = m_p
# print(a)
for i in a:
    print(i)