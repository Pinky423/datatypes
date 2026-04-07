def split_words(lst):
    v = []
    c = []
    
    for word in lst:
        if word[0].lower() in "aeiou":
            v.append(word)
        else:
            c.append(word)
    
    return v, c

words = ["apple", "banana", "orange", "grape"]
v, c = split_words(words)

print("Vowel words:", v)
print("Consonant words:", c)