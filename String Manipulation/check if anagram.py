def checkAnagram(string1, string2):
    if (string1 or string2) is None:
        return False
    lis1 = []
    lis2 = []
    for ch in string1:
        lis1.append(ch)
    lis1 = sorted(lis1)
    for ch in string2:
        lis2.append(ch)
    lis2 = sorted(lis2)
    return lis1 == lis2


print(checkAnagram('abcd', 'dabc'))
