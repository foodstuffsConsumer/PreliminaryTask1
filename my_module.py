import time

import requests

print(requests.__file__)

print("done")

API_URL = "https://www.dnd5eAPI_URL.co/API_URL/spells/"

spellbook = {}

def searcher(spell):
    response = requests.get(API_URL + spell.lower().replace(" ", "-"))
    if response.status_code == 200:
        spell_data = response.json()
        return {
            "name": spell_data["name"],
            "level": spell_data["level"],
            "description": spell_data["desc"][0]
        }
    else:
        print("Spell not found.")
        return None
print('')

def adder(spell):
    spellname = searcher(spell)
    if spellname:
        spellbook[spell] = spellname
        print(f"Added {spell} to your spellbook!")
print('')

def viewer():
    if not spellbook:
        print("Your spellbook is empty.")
    else:
        for spell in spellbook.values():
            print(f"{spell['name']} (Level {spell['level']}): {spell['description']}")
print('')

def remover(spell):
    if not spellbook:
        print("Your spellbook is empty.")
    else:
        if spellbook[spell]:
            spellbook.pop(spell)
            print(f"Removed {spell} from your spellbook.")
        else:
            print("Spell not found.")
print('')

def invalid():
    print("Please type in a valid command.")
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
            searcher(choice)
        elif choice == 'add':
            adder()
        elif choice == 'view':
            viewer()
        elif choice == 'remove':
            remover()
        else:
           invalid()
        
        time.sleep(1.5)