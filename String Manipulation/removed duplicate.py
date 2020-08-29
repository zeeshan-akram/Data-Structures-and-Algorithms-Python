def rotationCheck(word):
    removed = ''
    for ch in word:
        if ch not in removed:
            removed += ch
    return removed


print(rotationCheck('Trees'))
