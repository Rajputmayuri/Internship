"""1. Word Counter – Count words, characters, and sentences in a given text file."""

file_name = "word_count.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
        print("File Content:\n")
        print(text)

        # Count characters (excluding spaces)
        count_char = len(text.replace(" ", ""))
        print("\nTotal Characters (excluding spaces):", count_char)

        # Count words
        words = text.split()
        word_count = len(words)
        print("Total Words:", word_count)

        # Count sentences (basic approach)
        sentence_count = 0
        for ch in text:
            if ch in [".", "!", "?"]:
                sentence_count += 1
        print("Total Sentences:", sentence_count)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
