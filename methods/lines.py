def lines(text, lines):
    text1 = list(filter(None, text.split(sep='\n')))
    lines1 = lines.split()
    transformed_text = ""
    for i in range(len(text1)):
        if i % 4 + 1 in lines1:
            transformed_text += text1[i] + '\n'
        else:
            empty_words = ""
            for ew in range(len(text1[i])):
                empty_words += ' ' + '-' * len(text1[i][ew])
            transformed_text += empty_words + '\n'

    return transformed_text
