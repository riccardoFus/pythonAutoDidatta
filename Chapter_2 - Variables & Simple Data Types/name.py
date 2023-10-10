name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython");
print("Languages:\nPython\nC\nJavascript")
print("Languages:\n\tPython\n\tC\n\tJavascript")

favorite_language = "Python  "
print(f"'{favorite_language}'")
print(f"'{favorite_language.rstrip()}'") # removed temporily
# rstrip remove only whitespaces on the right, lstrip and strip respectively remove whitespaces on the left and both sides
print(f"'{favorite_language}'")
new_favorite_language = favorite_language.rstrip()
print(f"'{new_favorite_language}'")

message = "Hello Eric, would you like to learn some Python today?"
print(message)

name_author = "Albert Einstein"
quote = "A person who never made a mistake \n \tnever tried anything new"
print(f"\t{name_author} once said, \"{quote}\"")