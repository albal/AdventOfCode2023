data = file1 = open('input01.txt', 'r').readlines()

first = 0
last = 0
total = 0
sumt = 0

number_map = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}
replacements_dictionary = {'one': 'on1e', 'two': 'tw2o', 'three': 'thr3e', 'four': 'fo4ur', 'five': 'fi5ve',
                           'six': 'si6x', 'seven': 'sev7en', 'eight': 'ei8ght', 'nine': 'ni9ne'}

for line in data:
    for key, value in replacements_dictionary.items():
        line = line.replace(key, value)

    for char in line:
        if char.isnumeric():
            first = int(char) * 10
            break
    for char in line[::-1]:
        if char.isnumeric():
            last = int(char)
            break
    total = first + last
    sumt = sumt + total

print("Total is:", sumt)

