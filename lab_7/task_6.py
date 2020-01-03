def saddle_point(matrix):
    if len(matrix) == 1:
        return 0
    y = 0
    while len(matrix) > y:
        for i in matrix:
            l_min = min(i)
            l_index = i.index(l_min)
            for j in matrix:
                if l_min > j[l_index]:
                    return matrix.index(i), l_index
        return None
    y += 1


b = saddle_point([[0, 2, -1], [1, 2, -2]])
print(b)
