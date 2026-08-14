d=str(input("Enter a string: "))
word_count=0
char_count=0
space_count=0
if d:
    word_count=len(d.split())
    char_count=len(d)
    space_count=d.count(" ")
print(f"Number of words: {word_count}")
print(f"Number of characters: {char_count}")
print(f"Number of spaces: {space_count}")