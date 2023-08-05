"""
If the numbers 1 to 5 are written as "one,"
"two," "three," "four," "five," then the total
number of letters used is 3 + 3 + 5 + 4 + 4 = 19.

Problem: If the numbers 1 to 1000 (inclusive) are
written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342
(three hundred forty-two) contains 23 letters and 115
(one hundred fifteen) contains 20 letters. The use of
"and" when writing numbers is in compliance with British usage.
"""


def number_to_words(n: int) -> str:
    under_twenty = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    if n == 1000:
        return "onethousand"

    words = ""

    if n >= 100:
        words += under_twenty[n // 100 - 1] + "hundred"
        if n % 100 != 0:
            words += "and"

    if n % 100 >= 20:
        words += tens[n % 100 // 10 - 2]
        if n % 10 != 0:
            words += under_twenty[n % 10 - 1]
    elif n % 100 > 0:
        words += under_twenty[n % 100 - 1]

    return words


def count_letters_in_number_words(limit: int) -> int:
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters


print(count_letters_in_number_words(1000))
