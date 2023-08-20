"""
Using names.txt (right-click and 'Save Link/Target As...'),
a 46K text file containing over five thousand first names,
begin by sorting it into alphabetical order.

Then, working through each name, calculate the alphabetical
value for each name (where A=1, B=2, ..., Z=26), and multiply
this value by the name length. Sum all the values to obtain the
total score.

What is the total score of all names in the file?
"""


def calculate_name_score(name):
    return sum(ord(letter) - ord('A') + 1 for letter in name)


def total_name_scores(names):
    names.sort()
    total_score = 0
    for index, name in enumerate(names, start=1):
        score = calculate_name_score(name) * index
        total_score += score
    return total_score


with open("names.txt", "r") as file:
    names = file.read().replace('"', '').split(',')

result = total_name_scores(names)
print(total_name_scores(names))
