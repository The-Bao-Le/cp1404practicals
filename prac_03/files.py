FILENAME = "names.txt"

out_file = open(FILENAME, 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()