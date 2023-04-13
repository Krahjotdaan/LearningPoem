def quatrains(text, quatrains):
    text1 = list(filter(None, text.split('\n')))
    quatrains1 = quatrains.split()
    transformed_text = ""
    try:
        for i in quatrains1:
            for j in range((i - 1) * 4, (i - 1) * 4 + 4):
                transformed_text += text1[j]
            transformed_text += '\n'
            
    except IndexError:
        pass

    return transformed_text
