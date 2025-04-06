import my_module

def main():

    """Creates the interface for the program."""

    while True:
        print('\n======================')
        print('Spellbook Command Menu')
        print('======================')
        print('\nsearch - Search for a spell.')
        print('add - Add a spell to your personal spellbook.')
        print('view - Displays your personal spellbook.')
        print('remove - Removes a spell from your spellbook.')
        print('quit - Quits the menu.')
        rawcommand = input("\nInput a command: ")

        command = rawcommand.lower() # converts user input into lowercase automatically, preventing need for case-sensitivity

        if command == 'search':
            searchedspell = input('What spell would you like to search for? ')
            my_module.searcher(searchedspell)

        elif command == 'add':
            addedspell = input('What spell would you like to add? ')
            my_module.adder(addedspell)

        elif command == 'view':
            my_module.viewer()

        elif command == 'remove':
            if not my_module.spellbook:
                print("Your spellbook is empty.")
                my_module.time.sleep(1.5)
            else:
                removedspell = input('What spell would you like to remove? ')
                my_module.remover(removedspell)

        elif command == 'quit':
            print("Quitting...")
            quit() # built in function, don't have to define it or get it through a module
            
        else:
           my_module.invalid()

if __name__ == "__main__":
    main()