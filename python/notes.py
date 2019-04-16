notes_list = []

def printMenu():
    print("MAIN MENU =+=+=+=+=+=+=+=+=+")
    print("  Press a to add a note.")
    print("  Press d to delete a note.")
    print("  Press p to print all notes.")
    print("  Press q to quit.")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

def inputNote():
    n = []
    title = input("Enter title. ")
    n.append(title)
    note = input("Enter note. ")
    n.append(note)
    return n

def addNote(notes, new):
    notes.append(new)
    print("Note added!")

def deleteNote(notes, i):
    if len(notes) <= i:
        print("That note doesn't exist!")
        return

    notes.pop(i)
    print("Note " + str(i) + " deleted.")

def printNotes(notes):
    count = 0
    for n in notes:
        print(str(count))
        print(n[0])
        print(n[1])
        print()
        count += 1

def main():
    print("Notes program!!!")

    while True:
        printMenu()
        c = input("Input choice. ")

        if c == 'a':
            n = inputNote()
            addNote(notes_list, n)
        elif c == 'd':
            i = int(input("Enter number. "))
            deleteNote(notes_list, i)
        elif c == 'p':
            printNotes(notes_list)
        elif c == 'q':
            break;
        else:
            print("Invalid choice.")

main()