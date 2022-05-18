Discord-Bot for creating randomized DnD characters


1. Description

The projects' goal is to create a discord bot, that can be prompted by server members to generate a random Dungeons and Dragons
character, that includes: A character class, a character lineage and the six DnD stats strength (STR), dexterity (DEX), 
constitution (CON), intelligence (INT), wisdom (WIS) and charisma (CHA).

The class and lineage are randomly chosen from the lists coded in. The stats are generated according to the DnD rules
for rolling for stats. Per stat four D6 dice are rolled, the lowest one is dropped, the remaining three are added up.

Each class has a different priority for assigning stats. This fact is accounted for by the three different generation modes:
- Good: Assigns the generated stats according to the class priority. Highest priority stat gets the highest value, lowest
	priority stat gets the lowest value.
- Bad:	Assigns the generated stats in reverse to the class priority. Highest priority stat gets the lowest value, lowest
	priority stat gets the highest value.
- Random: Stats are assigns values as rolled, not afterward prioritization.

Each lineage gives multiple +2 or +1 increases to stats. These are added after the stats are assigned based on the class.

The app uses the discord.py package to interact with the Discord API, connect to Discord servers and reacted to user messages.

For storing the Discord API token a .env file is used, that is read by the app via the dotenv package.

The next step in the project is to build a Docker container in which the app can be hosted. I plan on using a Raspberry Pi 4
for hosting the app in my own network.


2. How to install and run the project

Currently, the project can be run by executing it via the cmd line."python3 main.py"
To install the required packages: "python3 -m pip install discord.py dotenv"
To run the program: "python3 main.py"


3. How to use the project

Add the bot to a server you want.
After it has joined the server, and successfully connected (shows success message via cmd line) you can type in the following
commands in Discord to interact with it:

!dnd-help:	Shows help prompt with the available commands
!dnd-good:	Generates a random character with a good stat spread for the generated class
!dnd-bad:	Generates a random character with a bad stat spread for the generated class
!dnd-random:	Generates a random character with a random stat spread without taking class into consideration


4. Credits

Creator:	Sebastian Werner	https://github.com/Se-Werner	https://www.linkedin.com/in/sebastian-werner-13a991191/

This app was created by using these resources:
https://realpython.com/how-to-make-a-discord-bot-python/
