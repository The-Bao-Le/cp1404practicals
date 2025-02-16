FILENAME = "names.txt"

out_file = open(FILENAME, 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()

in_file = open(FILENAME, 'r')
text = in_file.read()
in_file.close()
print(text)

with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)

with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)