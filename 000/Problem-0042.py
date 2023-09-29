"""
The nth term of the sequence of triangle
numbers is given by, tn = 0.5 * n * (n + 1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number
corresponding to its alphabetical position and
adding these values, we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55,
which is a triangle number.

If the word value is a triangle number, then we
shall call the word a triangle word.

How many words in the given text file (0042_words.txt)
are triangle words?
"""
import string


def triangle_number(n):
    return n * (n + 1) // 2


def word_value(word):
    return sum(ord(letter) - ord('A') + 1 for letter in word)


with open('0042_words.txt', 'r') as file:
    words = file.read().replace('"', '').split(',')

max_word_length = max(len(word) for word in words)
max_word_value = max_word_length * (ord('Z') - ord('A') + 1)

triangle_numbers = [triangle_number(n) for n in range(1, max_word_value + 1)]

count = sum(1 for word in words if word_value(word) in triangle_numbers)

print(count)
