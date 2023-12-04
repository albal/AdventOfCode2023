data = file1 = open('input01.txt', 'r').readlines()

first = 0
last = 0
total = 0
sumt = 0

number_map = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

for line in data:

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
