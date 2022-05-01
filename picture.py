def picture():
    picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
               [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

    for i in picture:
        line = ''
        for p in i:
            if p == 0:
                line += ' '
            else:
                line += '*'
        print(line)
