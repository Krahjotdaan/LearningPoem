def quatrains(text):
    text1 = list(filter(None, text.split('\n')))
    nums = list(map(int, input().split(',')))

    try:
        for i in nums:
            for j in range((i - 1) * 4, (i - 1) * 4 + 4):
                print(text1[j])
            print('\n')
            
    except IndexError:
        pass
