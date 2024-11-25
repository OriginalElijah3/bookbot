def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count = word_count(file_contents)
        print("--- Begin report of books/frankenstein.txt ---")
        print(count, "words found in the document")
        counts = char_count(file_contents)

        for key in counts:
            print("The character '"+ key + "' was found", counts[key], "times")

def word_count(book):
    words = []

    words = book.split()

    return len(words)

def char_count(book: str):
    words = book.split()
    counts = {}
    for word in words:
        for char in word:
            if char.isalpha():
                if char.lower() in counts:
                    counts[char.lower()] += 1
                else:
                    counts[char.lower()] = 1

    return counts

main()