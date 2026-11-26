name = input()

name_clean = name.replace(" ", "").lower()

if name[::] == name[::-1]:
    print("Palindrome Name")
else:
    print("Not a Palindrome")