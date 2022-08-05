#!/usr/bin/python3

''' defines function to prints text with 2 new lines after . ? and : '''


def text_indentation(text):
    ''' prints text with 2 new lines after . ? and : '''
    if not type(text) == str:
        raise TypeError('text must be a string')
    new_string = ""
    for i in range(len(text)):
        if text[i] in ".?:":
            new_string += (text[i]+'\n' * 2)
            while not text[i].isalpha():
                i += 1
            if text[i + 2]
        else:
            new_string += text[i]
    print(new_string)
