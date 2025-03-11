import time

def main():
    while True:
        print('======================')
        print('Spellbook Command Menu')
        print('======================')
        print('')
        print('search - Search for a spell.')
        print('add - Add a spell to your personal spellbook.')
        print('view - Displays your personal spellbook.')
        print('remove - Removes a spell from your spellbook.')
        print('')
        rawcommand = input("Input a command: ")

        command = rawcommand.lower()

        if command == 'search':
            print("doesn't work yet")
            print('')
        elif command == 'add':
            print("not yet buddy pal")
            print('')
        elif command == 'view':
            print("under construction")
            print('')
        elif command == 'remove':
            print("give time where time is due") 
            # did you know? the printed statement above is a reference. if you know what it is, you're based. based on what? idk man
            print('')
        else:
            print("dude this wouldn't be valid even if the program worked")
            print('')
        
        time.sleep(1.5)