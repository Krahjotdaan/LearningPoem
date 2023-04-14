def quatrains(text, quatrains):
    try:
        if quatrains is not None:
            text1 = list(filter(None, text.split('\n')))
            quatrains1 = list(map(int, quatrains.split()))
            quatrains1.sort()
            transformed_text = ""
            try:
                for i in quatrains1:
                    for j in range((i - 1) * 4, (i - 1) * 4 + 4):
                        transformed_text += text1[j] + '\n'
                    transformed_text += '\n'
                    
            except IndexError:
                pass

            return transformed_text
        
        else:
            return text
    
    except AttributeError:
        return text
