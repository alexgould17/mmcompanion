# Project Design Specifications
This is intended to be an all-inclusive list of classes, methods, data & i/o interfaces implemented (or to-be implemented) within the project.
## Python
Most, if not all, classes will use `__slots__` since we every one of them represents an already-existing set of data.

It would be nice to (eventually) have a way to read the original game data files or even save files directly via a script, but that is the farthest afield of all the functionality in this document.
### Classes
#### Game
Represents a user game playthru.
#### Area
Represents an overworld area.

Knows:
- Reset time
- Game (6/7/8/merge)
- ID (numerical id, loosely mapped to game attributes, mm6 will be 611-635 based on their position on the "grid" (Sweet Water 611 - New Sorpigal 635), mm7 will be in the 700's,  mm8 800's, merge area will be 001.)
- Adjacent areas
- Dungeon entrances
- Map
- Points of interest (should be labeled on the map)
- Monsters/monster groups present in world
- Quests given here
- Quests objectives here
- Any travel limitations (i.e. if it's impossible to get here before a certain point in the game (e.g. Regna mm8), or if it's closed after a certain point in the game (e.g. Clanker's Lab mm7))
- Coach & Boat schedules (where appropriate)
#### Dungeon
Represents a dungeon area (potentially a subclass of `Area` or derived from the same superclass).

Knows:
- Reset time
- Game (6/7/8/merge)
- ID (numerical ID, mm6/7/8 will be 600's/700's/800's respectively, merge interior cells will be 001)
- Exits to areas/other dungeons
- Map
- Points of interest (should be labeled on the map)
- Monsters/monster groups present in world
- Quests given here
- Quests objectives here
- Any travel limitations (i.e. if it's impossible to get here before a certain point in the game (e.g. Regna mm8), or if it's closed after a certain point in the game (e.g. Clanker's Lab mm7))
#### Monster
Represents a type of monster present in the game & contains all its relevant information. Unsure at the moment if one monster instance should refer to a group of monsters (e.g. goblin, hobogoblin & goblin lord from mm7) or if each one of those should be an instance & they should have some sort of group attribute.

Knows:
- Name
- Game (6/7/8/merge)
- Image (?)
- Max hp
- AC
- Attack type
- Attack damage
- Spell
- Resistances
- Statuses inflicted
- Notes (e.g. Boulders explode when they die)
#### Quest
Represents a quest, contains all the relevant information needed for completion & has a status based on the user's playthru (not received, in progress, completed, or eliminated). Eliminated is for when a choice in the playthru prevents completion of the quest, e.g. choosing the path of light in mm7 precludes you from receiving or completing dark path quests.

Knows:
- Status
- Game (6/7/8/merge)
- ID (numerical id, I think they're numbered internally, so use that if so, if not, make up something that works)
- Type (storyline, promotion, side)
- Prerequisite quests
- Items required
- Areas visited
- NPC that gives quest (`None` should mean you have the quest to start the game)
#### Items
Represents an item that can be in your inventory: weapons, armor, trinkets, quest items, ores, etc. Probably won't make a detailed inventory of these on the first pass, mainly interested in quest items.

Knows:
- Name
- Image (?)
- Type of item
- Item slot (`None` should mean unequippable)
- Enchantment (implement later when tracking items in specific saves, but leave a slot open for enchantments)
- If it is an artifact, relic, or quest item
- For quest items only, does it disappear after you complete the quest
- Main stat (damage for weapons, AC for armor pieces)
- Base value
- Total value (includes enchantment value)
- Description
#### Enchantment
Represents an enchantment that can be applied to an `Item`. For later implementation.

Knows:
- Name
- Description
- Numerical value (certain types of enchantments, e.g. "of Might", have a numerical value between 1 & 25 (inclusive of both) that determines the strength of the enchantment)
- Type of items it can be applied to
#### PlayerChar
Represents a character in the player's party (or in the Adventurer's Inn in Jadame).

Knows:
- Name
- Race, class & gender (mm8 chars won't use race, just class)
- Primary stats (array of 7 ints)
- Skills (list of tuples with name & level)
- Inventory (list of `Item`s)
#### NPC
Represents a character that can be interacted with that's not a player character, could be a teacher, quest giver, quest goal, etc.

Knows:
- Location (starting if they're mobile)
- Inside (boolean that's False if the person is a character on the adventure map, True if they're just behind a door somewhere)
- Name
- Quests given (list of `ID`s)
- Skills taught (tuple with name, level & cost)
- Notes (extra info)
#### TimeDate
Represents the time & date in-game (since it's different than in the real world), used to calculate resets, in relation to certain quests (e.g. mm6 druid promotion quests), etc.

Knows:
- Days since the beginning (int representing number of days elapsed since the game began, 1 Jan 1168 (I think))
- Minutes in the day (int representing the number of minutes elapsed since midnight)

Does:
- Prints readable string (`__str__`)
- Tells moon phase, month of year, day of week
## HTML
Interfaces:
- Data entry (should be in the .gitignore, this is for me to add/edit data to the game database)
- 
## Datafiles & Directory Structure