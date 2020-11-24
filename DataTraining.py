import numpy as np

print("hello world")

primes = [2, 3, 3, 4, 5]
for prime in primes:
    print(prime)

for x in range(1, 5):
    print(x)

count = 0
while count < 10:
    print(count)
    count = count + 1

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for num in numbers:
    if num % 2 == 0 & num != 360:
        print(num)
        break

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

numberslist = [23, -1, 2, 132, -3]
newnum = [int(num) for num in numberslist if num > 0]
print(newnum)

a = set([2, 3, 3, 5])
print(a)

b = [2, 3, 4]
print(b)

c = {2, 3, 44, 5}
print(c)

data = ('jack', 'son', 56.4)

format_string = "Hi %s %s, you current balance is $%s"
print(format_string % data)

import json


def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


# test code

salariesOrinal = '{"A":300,"B":600}'
newsalaries = add_employee(salariesOrinal, 'me', 800)
decode_salaries = json.loads(newsalaries)
print(decode_salaries['A'])
print(decode_salaries['B'])
print(decode_salaries['me'])

