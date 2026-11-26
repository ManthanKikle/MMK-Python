with open("notes.txt", "a") as notes:
    notes_IN = input()
    notes.write(notes_IN + '\n')

with open("notes.txt", "r") as notes:
    print(notes.read())

    
    