def find_words(words):

    row_T = 'qwertyuiop'
    row_H = 'asdfghjkl'
    row_B = 'zxcvbnm'
    result = []

    for word in words:
        lowercase_word = word.lower()

        # Check if all letters of the word are in the same row
        if all(letter in row_H for letter in lowercase_word) or \
           all(letter in row_B for letter in lowercase_word) or \
           all(letter in row_T for letter in lowercase_word):
            result.append(word)

    return result


words_array = ["Hello", "Alaska", "Dad", "Peace"]
filtered_words = find_words(words_array)

print(filtered_words)
