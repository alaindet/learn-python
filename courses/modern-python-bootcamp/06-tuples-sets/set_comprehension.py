set1 = {n for n in range(10)}
print(set1)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

set2 = {n**2 for n in range(5+1) if n % 2 == 1}
print(set2)  # {1, 9, 25}

all_vowels = 'aeiou'


def contains_all_vowels(sentence: str) -> bool:
    global all_vowels
    vowels_in_sentence = {ch for ch in sentence.lower() if ch in all_vowels}
    return len(vowels_in_sentence) == len(all_vowels)


print(
    contains_all_vowels('aeiou'),  # True
    contains_all_vowels('AEIOU'),  # True
    contains_all_vowels('hello'),  # False
    contains_all_vowels('toRUgitAE'),  # True
)
