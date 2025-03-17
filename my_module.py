import time

spellbook = {}

def searcher():
    print("doesn't work yet")
    print('')

def adder():
    print("not yet buddy pal")
    print('')

def viewer():
    print("under construction")
    print('')

def remover():
    print("give time where time is due") 
    # did you know? the printed statement above is a reference. if you know what it is, you're based. based on what? idk man
    print('')

def invalid():
    print("dude this wouldn't be valid even if the program worked")
    print('')

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
        rawchoice = input("Input a command: ")

        choice = rawchoice.lower()

        if choice == 'search':
            searcher()
        elif choice == 'add':
            adder()
        elif choice == 'view':
            viewer()
        elif choice == 'remove':
            remover()
        else:
           invalid()
        
        time.sleep(1.5)