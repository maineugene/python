def delete_vowels(phrase):
    '''Задача 2. Удаление гласных'''
    vowels = set('aeiuoAIOUE')
    result = ''
    for letter in phrase:
        if letter not in vowels:
            result += letter
    return result
phrase = input("enter phrase:")
without_vowels = delete_vowels(phrase)
print(without_vowels)

