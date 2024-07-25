def all_variants(text):
    for letter in text:
        yield letter
    for letter_index in range(len(text)):
        if letter_index == len(text)-1:
            yield text
            break
        yield text[letter_index] + text[letter_index+1]


a = all_variants("abc")
for i in a:
    print(i)
