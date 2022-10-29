from collections import deque

my_dict = {
    "rose": [1, 1, 1, 1],
    "tulip": [1, 1, 1, 1, 1],
    "lotus": [1, 1, 1, 1, 1],
    "daffodil": [1, 1, 1, 1, 1, 1, 1, 1]
}

vowels_collection = deque(input().split())
consonants_collection = input().split()

found_word = False
word = ""

while vowels_collection and consonants_collection:

    vowel = vowels_collection.popleft()
    consonant = consonants_collection.pop()

    for key, value in my_dict.items():
        if vowel in key:
            for i in range(key.count(vowel)):
                index = int(key.index(vowel)) + i
                value[index] = vowel

        if consonant in key:
            for i in range(key.count(consonant)):
                index = int(key.index(consonant)) + i
                value[index] = consonant

        for x, y in my_dict.items():
            if 1 not in y:
                found_word = True
                word = x
                break

        if found_word:
            break

    if found_word:
        break

if found_word:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")

if vowels_collection:
    print(f"Vowels left: {' '.join(vowels_collection)}")

if consonants_collection:
    print(f"Consonants left: {' '.join(consonants_collection)}")
