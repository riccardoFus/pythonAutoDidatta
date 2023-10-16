def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # pass -> failing silently
        print(f"Sorry, the file {filename} does not exist!")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def count_repeated_word(filename, word):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        occurences = contents.lower().count(word)
        return occurences

filenames = ['text_files/alice.txt', 'text_files/little_women.txt', 'text_files/moby_dick.txt']
for filename in filenames:
    count_words(filename)

for filename in filenames:
    print(f"Number of 'james' in {filename}: {count_repeated_word(filename, 'james')}")
    
for filename in filenames:
    print(f"Number of 'alice' in {filename}: {count_repeated_word(filename, 'alice')}")

for filename in filenames:
    print(f"Number of 'the ' in {filename}: {count_repeated_word(filename, 'the ')}")