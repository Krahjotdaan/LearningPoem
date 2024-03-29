def first_word(text):
    text1 = list(filter(None, text.split(sep='\n')))
    transformed_text = ""
    for i in range(len(text1)):
        tmp = text1[i].split()
        empty_words = ""
        for ew in range(1, len(tmp)):
            empty_words += ' ' + '-' * len(tmp[ew])

        transformed_text += tmp[0] + empty_words + '\n'
        if (i + 1) % 4 == 0:
            transformed_text += '\n'

    return transformed_text
