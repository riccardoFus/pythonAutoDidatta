filename = "C:\\Users\\User\\Desktop\\Riccardo Uni\\python_Crash_Course\\Chapter_10 - File & Exceptions\\text_files\\output.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming")

with open(filename, 'a') as file_object:
    file_object.write("\nI love creating apps that run in the browser")