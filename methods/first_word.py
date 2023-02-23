def first_word(text):
    lines = list(filter(None, text.split(sep='\n')))
    for i in range(len(lines)):
        tmp = lines[i].split()
        print(tmp[0])
        if (i + 1) % 4 == 0:
            print('')
