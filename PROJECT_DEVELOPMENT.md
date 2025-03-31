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
The program should run programs reliably.

# Design

# Development