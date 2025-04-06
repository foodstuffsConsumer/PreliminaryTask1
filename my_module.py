import time

import requests

API_URL = "https://www.dnd5eapi.co/api/2014/spells/"

spellbook = {}

# every instance of time.sleep() pauses the program for a certain amount of time, making the program less jarring to use

def finder(spelltofind):

    """Returns information about a spell for use with the adder() function."""

    formattedspell = spelltofind.lower().replace(" ", "-") + "/"
    response = requests.get(API_URL + formattedspell)
    if response.status_code == 200:
        spell_data = response.json()
        return {
            'name': spell_data["name"],
            'level': spell_data["level"],
            'description': spell_data["desc"][0]
        }
    
    elif response.status_code == 404: # status code 404 means the spell can't be found
        print("Spell not found.")
        time.sleep(1.5)
        return None

    else:
        print(f"Something went wrong with the API! Error code: {response.status_code}")
        time.sleep(1.5)
        return None

def searcher(searchedspell):

    """Prints information about a spell."""

    formattedspell = searchedspell.lower().replace(" ", "-") + "/"
    response = requests.get(API_URL + formattedspell)
    if response.status_code == 200:
        spell_data = response.json()
        print("\n[SPELL] - " + spell_data["name"])
        print("[LEVEL] - " + str(spell_data["level"]))
        print("[DESCRIPTION] - " + spell_data["desc"][0])
        
        time.sleep(1.5)
        
        try:
            backtomenu = input('\nInput anything when you would like to return to the Command Menu. ')
            if backtomenu:
                return None
        except:
            return None

    elif response.status_code == 404:
        print("Spell not found.")
        time.sleep(1.5)

    else:
        print(f"Something went wrong! Error code: {response.status_code}")
        time.sleep(1.5)

def adder(addedspell):

    """Adds a spell into the spellbook with the help of the finder() function."""

    trueaddedspell = addedspell.title() # makes the spell names look good. also makes them not case-sensitive when removing them
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

    """Views all spells currently stored in the spellbook."""

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

        try:
            backtomenu = input('\nInput anything when you would like to return to the Command Menu. ')
            if backtomenu:
                return None
        except:
            return None

def remover(removedspell):
    
    """Removes a spell from the spellbook."""

    trueremovedspell = removedspell.title()
    if trueremovedspell in spellbook:
        spellbook.pop(trueremovedspell)
        print(f"Removed {trueremovedspell} from your spellbook.")
    else:
        print("Spell not found.")
    time.sleep(1.5)

def invalid():

    """Prints an error message in case of an invalid command."""

    print("Please type in a valid command.")
    time.sleep(1.5)