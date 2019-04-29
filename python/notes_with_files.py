notes_list = []

def readNotes():
    global notes_list
    try:
        file = open("saved_notes.txt", "r")
        while 1:
            line1 = file.readline()
            if not line1:
                break
            line2 = file.readline()
            notes_list.append([line1.replace("\n", ""), line2.replace("\n", "")])

        file.close()
    except:
        notes_list = []

def saveNotes():
    global notes_list
    file = open("saved_notes.txt", "w")
    for i in notes_list:
        file.writelines('\n'.join(i))
        file.write('\n')
    file.close()

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
    readNotes()

    while True:
        printMenu()
        c = input("Input choice. ")

        if c == 'a':
            n = inputNote()
            addNote(notes_list, n)
            saveNotes()
        elif c == 'd':
            i = int(input("Enter number. "))
            deleteNote(notes_list, i)
            saveNotes()
        elif c == 'p':
            printNotes(notes_list)
        elif c == 'q':
            break;
        else:
            print("Invalid choice.")

try:
    main()
    print("\nProgram exited successfully.")
except KeyboardInterrupt:
    print("\nProgram was interrupted.")
except Exception as e:
    print("\nProgram encountered an error. Message details:")
    print(str(e))

