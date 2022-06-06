def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    first_ch = sentence[0] if length > 0 else None
    my_tuple += (length,)
    my_tuple += (first_ch,)
    return my_tuple
