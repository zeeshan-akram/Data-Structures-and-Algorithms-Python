def capitalize(string):
    capi = string.replace(' +', ' ').split()
    new_string = ''
    for word in capi:
        word = word.capitalize()
        new_string += word + ' '
    return new_string


print(capitalize('TREES ARE BEAUTIFUL'))
