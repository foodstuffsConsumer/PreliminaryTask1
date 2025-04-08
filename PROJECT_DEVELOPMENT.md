# **11SE TASK 1 2025 - SPELLBOOK APPLICATION**

# Requirements Definition

## Functional Requirements
The program's capabilities must include:

- Searching for spells by name, and viewing their level and description
- Storing spells in a spellbook for later viewing or removal
- Viewing all your spells in the spellbook, including their level and description
- Removing unneeded spells from the spellbook

## Non-Functional Requirements
The program should:

- Be easy to navigate and operate, with a text-based GUI
- Run consistently and quickly
- Handle invalid inputs and errors gracefully
- Be able to recognise commands in both uppercase and lowercase

# Determining Specifications

## Functional Specifications

### User Requirements
The user needs to be able to:
- Search for spells, and then add them to a spellbook
- View their current spellbook, and remove unwanted spells

### Input & Output
Inputs - The user should be able input text commands for certain functions. These inputs include:

- search - Searches for spells
- spellbook - Views your current spellbook
- add - Adds a spell to your spellbook
- remove - Removes a spell from your spellbook

Outputs - The program should respond to user requests by displaying tables, containing spells either searched or contained in the spellbook. It should also add or remove spells from the spellbook at the user's request.

### Core Features

At its core, the program should be able to:

- Search for spells
- Add spells to a spellbook
- View all spells currently in the spellbook
- Remove spells from the spellbook

### User Interaction

The GUI will be text-based, with users manually inputting commands for the program. On launch, the program will automatically provide a list of commands and their functions.

### Error Handling

In the event of an error, the program will display an error message.

## Non-Functional Specifications

### Performance
The program should be able to successfully respond to programs under 2 seconds.

### Usability
The program should be able to recognise commands in lowercase, uppercase, and a mixture.

### Reliability
The program should run programs reliably without encountering frequent errors.

# Testing & Debugging

## 10/03/2025

Created and worked on the initial markdown file for documentation, completing Requirements Definition and Determining Specifications. Added an interface to the main.py program, but with no functions yet.

## 17/03/2025

Moved the placeholder code from the interface into functions.

## 19/03/2025

Created actual code for the functions, which should have allowed the user to search, add, view, and remove spells from the spellbook. Encountered an error with the `requests` import not being able to be resolved from source.

## 24/03/2025

Fixed the error, and also fixed a bug with the `viewer()` function, which was meant to display information about all the spells in the spellbook, essentially completing the development phase of the project.

## 25/03/2025

Created a proper README and requirements.txt file.

## 31/03/2025

Added seperate error messages for searching and adding spells; the program will now display different messages from the inputted spell being invalid, or something else being wrong with the API entirely.

# Maintenance

The API URL may need tweaking in the future if the link is altered in any way.
If the program becomes incompatible with newer Python versions for any reason, the code will require further updates.
If a user finds a bug with the program after deployment,
- They should send a message regarding the bug with the error message
- The code in the relevant section will be reviewed and the bug attempted to fix
- If debugging is completely successful, push the debugged version of the program for public use
- If debugging is unsuccessful for any reason such as time constraints or otherwise, implement a temporary solution such as graceful error handling and push it