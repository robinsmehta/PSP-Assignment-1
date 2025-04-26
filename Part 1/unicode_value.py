'''Print Unicode encoding for each character in your name'''

name = input("Enter your name: ")

for char in name:
    print(f"Character: {char} -> Unicode: {ord(char)}")
