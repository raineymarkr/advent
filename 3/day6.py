import re

f = open(r'3/instructions.txt', 'r')
instructions = f.read()

regex = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', re.IGNORECASE)
uncorrupted = re.findall(regex, instructions)




def number_extractor(string):
    regex_numbers = re.compile(r'\d+')
    numbers = re.findall(regex_numbers, string)
    return int(numbers[0]) * int(numbers[1])

total = 0
mult_flag = True

def conditional_extractor(string, total):
    global mult_flag

    if string == "don't()":
        mult_flag = False
    elif string == "do()":
        mult_flag = True
    elif mult_flag == True:
        total += number_extractor(string)
    return total

for i in range(0, len(uncorrupted)):
    total = conditional_extractor(uncorrupted[i], total)


print(total)