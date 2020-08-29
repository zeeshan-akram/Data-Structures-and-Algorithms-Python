vowels = ['A', 'E', 'O', 'U', 'I']
string = input('Enter String>').upper()
vowel_count = 0
for vowel in vowels:
    vowel_count += string.count(f'{vowel}')
print(vowel_count)
