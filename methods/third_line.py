def third_line(text):
    lines = list(filter(None, text.split(sep='\n')))
    for i in range(len(lines)):
        if i % 4 == 2:
            print(lines[i])
        else:
            print('X')

        if (i + 1) % 4 == 0:
            print('')
