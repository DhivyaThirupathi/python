import os
poem_file = "poem.txt"
with open(poem_file, "w") as file:
    file.write(
        """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are."""
    )
print("Poem file created successfully.")

file_size = os.path.getsize(poem_file)
print(f"Size of '{poem_file}': {file_size} bytes")


print("\nFirst four lines of the poem:")
with open(poem_file, "r") as file:
    for _ in range(4):
        print(file.readline().strip())


with open(poem_file, "r") as file:
    words = file.read().split()
longest_word = max(words, key=len)
print(f"\nLongest word in the poem: {longest_word}")


word_to_count = input("\nEnter a word to count its frequency: ").strip()
word_count = words.count(word_to_count)
print(f"The word '{word_to_count}' appears {word_count} times in the poem.")


with open(poem_file, "r") as file:
    line_count = sum(1 for _ in file)
print(f"\nNumber of lines in the poem: {line_count}")


copy_file = "poem_copy.txt"
with open(poem_file, "r") as src, open(copy_file, "w") as dest:
    dest.write(src.read())
print(f"\nContents copied to '{copy_file}' successfully.")
