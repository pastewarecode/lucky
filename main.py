# context manager
with open("mydefaults.ini.txt") as ini_file:
    data = ini_file.read()

lines = data.split("\n")
key_value_ini = dict()
# print(len(lines))
for line in lines:
    if "=" in line:
        fields = line.split("=")
        key_value_ini[fields[0]] = fields[1]
print(key_value_ini)


letter_counter = 0

for letter in data:
    if letter.isalpha():
        letter_counter += 1

number_counter = 0

for number in data:
    if number.isnumeric():
        number_counter += 1

with open("outputs.txt", "w") as outputs:
    outputs.write(f"Amount of letters: {letter_counter}\n")
    outputs.write(f"Amount of numbers: {number_counter}")

