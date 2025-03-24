import time

import requests

API_URL = "https://www.dnd5eapi.co/api/2014/spells/"

spellbook = {}

def searcher(searchedspell):
    formattedspell = searchedspell.lower().replace(" ", "-") + "/"
    response = requests.get(API_URL + formattedspell)
    if response.status_code == 200:
        spell_data = response.json()
        print("\n[NAME] - " + spell_data["name"])
        print("[LEVEL] - " + str(spell_data["level"]))
        print("[DESCRIPTION] - " + spell_data["desc"][0])
        
        time.sleep(1.5)

        backtomenu = input('\nInput anything when you would like to return to the Command Menu. ')
        if backtomenu:
            return None

    else:
        print("Spell not found.")
        time.sleep(1.5)

def finder(spelltofind):
    formattedspell = spelltofind.lower().replace(" ", "-") + "/"
    response = requests.get(API_URL + formattedspell)
    if response.status_code == 200:
        spell_data = response.json()
        return {
            'name': spell_data["name"],
            'level': spell_data["level"],
            'description': spell_data["desc"][0]
        }
    else:
        print("Spell not found.")
        time.sleep(1.5)
        return None

def adder(addedspell):
    trueaddedspell = addedspell.title()
    spell = finder(trueaddedspell)
    if spell:
        if trueaddedspell not in spellbook:
            spellbook[trueaddedspell] = spell
            print(f"Added {trueaddedspell} to your spellbook!")
            time.sleep(1.5)
        else:
            print("You already have this spell!")
            time.sleep(1.5)

def viewer():
    if not spellbook:
        print("Your spellbook is empty.")
        time.sleep(1.5)
    else:
        print('')
        for spell in spellbook.values():
            print(f"{spell['name']} [LEVEL {spell['level']}]")
            print(spell['description'])
            print('')

        time.sleep(1.5)
        backtomenu2 = input('\nInput anything when you would like to return to the Command Menu. ')
        if backtomenu2:
            return None

def remover(removedspell):
    trueremovedspell = removedspell.title()
    if trueremovedspell in spellbook:
        spellbook.pop(trueremovedspell)
        print(f"Removed {trueremovedspell} from your spellbook.")
    else:
        print("Spell not found.")
    time.sleep(1.5)

def invalid():
    print("Please type in a valid command.")
    time.sleep(1.5)

def main():
    while True:
        print('\n======================')
        print('Spellbook Command Menu')
        print('======================')
        print('\nsearch - Search for a spell.')
        print('add - Add a spell to your personal spellbook.')
        print('view - Displays your personal spellbook.')
        print('remove - Removes a spell from your spellbook.')
        print('quit - Quits the menu.')
        rawchoice = input("\nInput a command: ")

        choice = rawchoice.lower()

        if choice == 'search':
            searchedspell = input('What spell would you like to search for? ')
            searcher(searchedspell)
        elif choice == 'add':
            addedspell = input('What spell would you like to add? ')
            adder(addedspell)
        elif choice == 'view':
            viewer()
        elif choice == 'remove':
            if not spellbook:
                print("Your spellbook is empty.")
                time.sleep(1.5)
            else:
                removedspell = input('What spell would you like to remove? ')
                remover(removedspell)
        elif choice == 'quit':
            print("Quitting...")
            quit()
        else:
           invalid()