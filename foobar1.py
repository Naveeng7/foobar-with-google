def solution(s):
    # Your code heredef solution(s):
    dct = {'a': '100000',
           'b': '110000',
           'c': '100100',
           'd': '100110',
           'e': '100010',
           'f': '110100',
           'g': '110110',
           'h': '110010',
           'i': '010100',
           'j': '010110',
           'k': '101000',
           'l': '111000',
           'm': '101100',
           'n': '101110',
           'o': '101010',
           'p': '111100',
           'q': '111110',
           'r': '111010',
           's': '011100',
           't': '011110',
           'u': '101001',
           'v': '111000',
           'w': '010111',
           'x': '101101',
           'y': '101111',
           'z': '101011',
           'cap' : '000001',
           'whitespace': '000000'
           }

    sol = ''
    for k in range(len(s)) :
        if s[k].isupper() == True:
                sol = sol + dct.get('cap')
        if s[k].isspace() == True:
                sol = sol + dct.get('whitespace')
        for i,j in dct.items():
            if i == s[k].lower():
                x = i
                sol = sol + j


    return sol