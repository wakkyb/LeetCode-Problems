import time
import string
def most_common_word(paragraph, banned):
    punc = "!?',;."
    word_base = {}

    modified_words = [''.join(' ' if char in punc else char for char in word) for word in paragraph.split()]
    paragraph = ' '.join(modified_words).lower()

    paragraph = [word.strip(string.punctuation) for word in paragraph.split() if
                 word.strip(string.punctuation).isalnum()]

    for word in paragraph:

        if (word not in word_base) and (word not in banned):
            word_base[word] = 1
        elif word in word_base:
            word_base[word] += 1

    return max(word_base, key=word_base.get)

para = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

start_time = time.time()

print(most_common_word(para, banned))

end_time = time.time()

runtime = ((end_time - start_time)*1000)

print(runtime)




