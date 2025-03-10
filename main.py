import time

def main():
    while True:
        print('---')
        print('Spellbook Command Menu')
        print('---')
        print('search - Search for a spell.')
        print('add - Add a spell to your personal spellbook.')
        print('spellbook - Displays your personal spellbook.')
        print('remove - Removes a spell from your spellbook')
        print('---')
        rawcommand = input("Choose a command: ")

        command = rawcommand.lower()

        if command == 'search':
            print("doesn't work yet")
        elif command == 'add':
            print("sorry but no")
        elif command == 'spellbook':
            print("under construction")
        elif command == 'remove':
            print("Give time where time is due. (i stole that line from an obscure game did you like it)")
        else:
            print("dude this wouldn't be valid even if the program worked")
        
        time.sleep(2)

if __name__ == "__main__":
    main()