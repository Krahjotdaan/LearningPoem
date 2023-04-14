def lines(text, lines):
    try:
        lines1 = list(map(int, lines.split()))
        if lines is not None and len(lines1) != 0:
            text1 = list(filter(None, text.split('\n')))  
            lines1.sort()
            transformed_text = ""
            for i in range(len(text1)):
                if i % 4 + 1 in lines1:
                    transformed_text += text1[i] + '\n'
                else:
                    empty_words = ""
                    for ew in range(len(text1[i])):
                        empty_words += '-' * len(text1[i][ew])
                    transformed_text += empty_words + '\n'
                
                if (i + 1) % 4 == 0:
                    transformed_text += '\n'

            return transformed_text
        
        else:
            return text
    
    except AttributeError:
        return text
