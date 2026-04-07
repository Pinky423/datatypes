def split_string(s):
    vowels = ""
    others = ""
    
    for ch in s:
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            others += ch
    
    return vowels, others

v, o = split_string("hello")
print("Vowels:", v)
print("Others:", o)