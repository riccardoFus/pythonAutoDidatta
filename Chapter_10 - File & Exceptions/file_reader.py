filename = "C:\\Users\\User\\Desktop\\Riccardo Uni\\python_Crash_Course\\Chapter_10 - File & Exceptions\\text_files\\pi_digits.txt"

with open(filename) as file_object:
    contents = file_object.read()
    contents.rstrip()
print(contents.rstrip())

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(f"{pi_string[:52]}")