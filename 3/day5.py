import re

f = open(r'3/instructions.txt', 'r')
instructions = f.read()

regex = re.compile(r'mul\(\d+,\d+\)', re.IGNORECASE)
uncorrupted = re.findall(regex, instructions)

def number_extractor(string):
    regex_numbers = re.compile(r'\d+')
    numbers = re.findall(regex_numbers, string)
    return int(numbers[0]) * int(numbers[1])

total = 0

for i in range(0, len(uncorrupted)):
    total += number_extractor(uncorrupted[i])

print(total)