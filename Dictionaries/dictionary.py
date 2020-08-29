dict = {

}

string = 'a pine apple'
for ch in string:
    if ch not in dict:
        dict[ch] = 1
    else:
        dict[ch] = dict[ch] + 1
for key in dict.keys():
    if dict[key] == 1:
        print(key)
        break