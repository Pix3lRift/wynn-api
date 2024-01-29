import http.client
import json
from typing import Union

def __fetch(path: str) -> dict:
    conn = http.client.HTTPSConnection("api.wynncraft.com")
    conn.request("GET", f"/v3{path}")
    res = conn.getresponse()
    
    responseData = res.read().decode("utf-8")
    conn.close()

    return json.loads(responseData)

def getPlayer(username:str=None, uuid:str=None, fullStats:bool=False) -> dict:
    """
    ## Player Info
    Get all kind of information about a player.
    Use either username or uuid.

    Parameters:
    - username (str): Username of the player
    - uuid (str): UUID of the player
    - fullStats (bool): When true, get all characters (classes) of the player too.

    Returns:
    {
        "username": str,
        "online": bool,
        "server": str,
        "activeCharacter": str or None,
        "uuid": str,
        "rank": str,
        "rankBadge": str, # URL to the badge SVG in the Wynncraft CDN (only path)
        "legacyRankColour": {
            "main": str,
            "sub": str
            },
        "shortenedRank": str,
        "supportRank": str,
        "veteran": bool,
        "firstJoin": str,
        "lastJoin": str,
        "playtime": int,
        "guild": {
            "name": str,
            "prefix": str,
            "rank": str,
            "rankStars": str
        },
        "globalData": {
            "wars": int,
            "totalLevels": int,
            "killedMobs": int,
            "chestsFound": int,
            "dungeons": {
                "total": int,
                "list": {
                    "Dungeon Name": int # Number of total completions on all characters
                    [...]
                }
            },
            "raids": {
                "total": int,
                "list": {
                    "Raid Name": int # Number of total completions on all characters
                    [...]
                }
            },
            "completedQuests": int,
            "pvp": {
                "kills": int,
                "deaths": int
            }
        },
        "forumLink": int or None,
        "ranking": {
            "Ranking Type": int
            [...]
        },
        "publicProfile": bool
    }
    """
    if (username is not None and uuid is None) or (username is None and uuid is not None):
        if fullStats:
            return __fetch(f"/player/{username or uuid}?fullResult")
        else:
            return __fetch(f"/player/{username or uuid}")
    else:
        raise TypeError('Invalid parameters provided: Either username or uuid is required')

def getPlayerCharacterList(username:str=None, uuid:str=None) -> dict:
    """
    ## Character List
    Get a player's character (class) list.
    Use either username or uuid.

    Parameters:
    - uuid (str): UUID of the player
    - characterUUID (str): The player's character's UUID (get by using getPlayerCharacterList() )

    Returns:
    {
        "characterUuid": {
            "type": str,
            "nickname": str,
            "level": int,
            "xp": int,
            "xpPercent": int,
            "totalLevel": int,
            "gamemode": [
                "hunter",
                "hardcore",
                # [...]
            ],
        },
        # [...]
    }
    """
    if (username is not None and uuid is None) or (username is None and uuid is not None):
        return __fetch(f"/player/{username or uuid}/characters")
    else:
        raise TypeError('Invalid parameters provided: Either username or uuid is required')

def getPlayerCharacter(username:str=None, uuid:str=None, characterUUID:str=None) -> dict:
    """
    Get all kind of information about a player's character (class).
    Use either username or uuid.

    Parameters:
    - username (str): Username of the player
    - uuid (str): UUID of the player
    - characterUUID(str): The player's character's UUID (get by using getPlayerCharacterList() )

    Returns:
    {
        "type": str,
        "nickname": str,
        "level": int,
        "xp": int,
        "xpPercent": int,
        "totalLevel": int,
        "wars": int,
        "playtime": int,
        "mobsKilled": int,
        "chestsFound": int,
        "blocksWalked": int,
        "itemsIdentified": int,
        "logins": int,
        "deaths": int,
        "discoveries": int,
        "pvp": {
            "kills": int,
            "deaths": int,
        },
        "gamemode": [
            "hunted",
            "hardcore",
            # [...]
        ],
        "skillPoints": {  # Can be empty if !playerProfile
            "strength": int,
            "dexterity": int,
            "intelligence": int,
            "defence": int,
            "agility": int
        },
        "professions": {
            "fishing": {
                "level": int,
                "xpPercent": int
            },
            "mining": {
                "level": int,
                "xpPercent": int
            },
            # [...]
        },
        "dungeons": {
            "total": int,
            "list": {
                "Dungeon Name": int
                # [...]
            }
        } or None,
        "raids": {
            "total": int,
            "list": {
                "Raid Name": int
                # [...]
            }
        } or None,
        "quests": [
            "Quest Name",
            # [...]
        ],
    }
    """
    if (characterUUID is None): raise TypeError('Parameter characterUUID is required')
    if (username is not None and uuid is None) or (username is None and uuid is not None):
        return __fetch(f"/player/{username or uuid}/characters/{characterUUID}")
    else:
        raise TypeError('Invalid parameters provided: Either username or uuid is required')

def getPlayerCharacterAbilityMap(username:str=None, uuid:str=None, characterUUID:str=None) -> dict:
    """
    ## Player's Ability Map
    Get a player's ability map on a specific character.
    Use either username or uuid.

    Parameters:
    - username (str): Username of the player
    - uuid (str): UUID of the player
    - characterUUID (str): The player's character's UUID (get by using getPlayerCharacterList() )

    Returns:
    {
        "pages": int,
        "map": [
            {
                "type": "ability",
                "coordinates": {
                    "x": int,
                    "y": int
                },
                "meta": {
                    "icon": str,  # Minecraft legacy item id e.g. 275:67
                    "page": int,
                    id": str  # Internal id of the ability, abilities in AT response are refered by the same id
                },
                "familiy": [  # Ability ids listed here are abilities connected to the current one
                    "ability1"
                    # [...]
                
            },
            {
                "type": "connector",
                "coordinates": {
                    "x": int,
                    "y": int
                },
                "meta": {
                    "icon": "connector_up_down",
                    # Connector icon syntax is both direction clockwise like right_left or right_down_left
                    "page": int
                },
                "family": [  # Ability ids listed here are abilities assiciated to this connector
                    "ability1",
                    # [...]
                ]
            },
            # [...]
        ]
    }
    """
    if (characterUUID is None): raise TypeError('Parameter characterUUID is required')
    if (username is not None and uuid is None) or (username is None and uuid is not None):
        return __fetch(f"/player/{username or uuid}/characters/{characterUUID}/abilities")
    else:
        raise TypeError('Invalid parameters provided: Either username or uuid is required')

def getOnlinePlayers(identifier:Union["username","uuid"], server:str or int or list) -> dict:
    """
    ## Online Players
    Get currently online players (on specific servers).

    Parameters:
    - identifier (Union["username","uuid"]): How players should be identified (by name or by UUID)
    - server (str or int or list): Format: "WC1" or 1 or ["WC1", "2"]

    Returns:
    {
        "onlinePlayers": int,
        "players": {
            "playerName": "WC1",
            "playerName": "WC43",
            # [...]
        }
    }
    """
    return __fetch(f"/player?identifier={identifier}&server={server}")

def getGuild(name:str=None, prefix:str=None, identifier:Union["username","uuid"]="username") -> dict:
    """
    ## Guild Info
    Get all kind of information about a player.
    Use either name or prefix.

    Parameters:
    - name (str): The name of the guild
    - prefix (str): Prefix of the guild
    - identifier (Union["username","uuid"]): How players should be identified (by name or by UUID)

    Returns:
    {
        "uuid": str,
        "name": str,
        "prefix": str,
        "level": int,
        "xpPercent": int,
        "territories": int,
        "wars": int,
        "created": str,
        "members": {
            "total": int,
            "owner": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "guildRank": int,
                    "joined": str,
                }
            },
            "chief": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "guildRank": int,
                    "joined": str,
                },
                # [...]
            },
            "strategist": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "guildRank": int,
                    "joined": str,
                },
                # [...]
            },
            "captain": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "guildRank": int,
                    "joined": str,
                },
                # [...]
            },
            "recruiter": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "guildRank": int,
                    "joined": str,
                },
                # [...]
            },
            "recruit": {
                "<username/uuid>": {
                    "<username/uuid>": str,
                    "online": bool,
                    "server": str or None,
                    "contributed": int,
                    "contributionRank": int,
                    "joined": str,
                },
                # [...]
            }
        },
        "online": int,
        "banner": {
            "base": str,
            "tier": int,
            "structure": str,
            "layers": [
                {
                    "colour": str,
                    "pattern": str
                },
                # [...]
            ]
        },
        "seasonRanks": {
            "1": {
                "rating": int,
                "finalTerritories": int
            }
            # [...]
        }
    }
    """
    if (name is not None and prefix is None) or (name is None and prefix is not None):
        if prefix:
            return __fetch(f"/guild/prefix/{prefix}?identifier={identifier}")
        else:
            return __fetch(f"/guild/{name}?identifier={identifier}")
    else:
        raise TypeError('Invalid parameters provided: Either name or prefix is required')

def getGuildsList(identifier:Union["username","uuid"]) -> dict:
    """
    ## Guild List
    Get all existing guilds.

    Parameters:
    - identifier (Union["username","uuid"]): How players should be identified (by name or by UUID)

    Returns:
    # identifier = uuid
    {
        "guildUuid": {
            "name": "name",
            "prefix": "prefix",
            # [...]
        },
        # [...]
    }

    # identifier = name
    {
        "guildName": {
            "uuid": "uuid",
            "prefix": "prefix",
            # [...]
        },
        # [...]
    }
    """
    return __fetch(f"/guild/list/guild?identifier={identifier}")

def getTerritoryList() -> dict:
    """
    ## Territories
    Get a list of all territories and their infos (the guild currently owning it, when it was acquired and its location).

    Returns:
    {
        "territoryName": {
            "guild": {
                "uuid": str,
                "name": str,
                "prefix": str
            },
            "acquired": str,
            "location": {
                "start": [
                    int,
                    int
                ],
                "end": [
                    int,
                    int
                ]
            }
        },
        # [...]
    }
    """
    return __fetch("/guild/list/territory")

def getNews() -> dict:
    """
    ## News
    Get the latest news about wynncraft.

    Returns:
    [
        {
            "title": str,
            "date": str,
            "forumThread": str,
            "author": str,
            "content": str,
            "comments": str
        },
    ]
    """
    return __fetch("/latest-news")

def getClasses() -> dict:
    """
    ## Classes
    Get all classes with thier overall difficulty.

    Returns:
    {
        "className": {
            "name": str,
            "overallDifficulty": int
            },
            # [...]
    }
    """
    return __fetch("/classes")

def getClassInfo(className:Union["warrior","archer","mage","assassin","shaman"]) -> dict:
    """
    ## Class Info
    Get infos about a class (like ID, name, lore, etc...).

    Parameters:
    - className (Union["warrior","archer","mage","assassin","shaman"]): The name of the class (non-donor, lowercase)

    Returns:
    {
        "id": str,
        "name": str,
        "lore": str,
        "overallDifficulty": int,
        "archetypes": {
            "archetypeId": {
                "name": str,
                "difficulty": int,
                "damage": int,
                "defence": int,
                "range": int,
                "speed": int
            },
        # [...]
        }
    }
    """
    return __fetch(f"/classes/{className}")

def getQuestsCount() -> dict:
    """
    ## Quests
    Get the count of quests (including mini-quests).

    Returns:
    {
        "quests": int
    }
    """
    return __fetch("/map/quests")

def getMapLocations() -> dict:
    """
    ## Map Locations
    Get all markers on the map. https://map.wynncraft.com/

    Returns:
    [
        {
            "name": str,
            "icon": str,
            "x": int,
            "y": int,
            "z": int
        },
        # [...]
    ]
    """
    return __fetch("/map/locations/markers")

def getPlayerLocations() -> dict:
    """
    ## Players on the map
    Get all players (yourself, friends, party members, guild members) on the map. https://map.wynncraft.com/

    Returns:
    [
        {
            "uuid": str,
            "name": str,
            "nickname": str,
            "server": str,
            "x": int,
            "y": int,
            "z": int,
            "friends": [
                {
                    "uuid": str,
                    "name": str,
                    "nickname": str,
                    "server": str,
                    "x": int,
                    "y": int,
                    "z": int
                },
                # [...]
            ],
            "party": [
                {
                    "uuid": str,
                    "name": str,
                    "nickname": str,
                    "server": str,
                    "x": int,
                    "y": int,
                    "z": int
                },
                # [...]
            ],
            "guild": [
                {
                    "uuid": str,
                    "name": str,
                    "nickname": str,
                    "server": str,
                    "x": int,
                    "y": int,
                    "z": int
                },
                # [...]
            ]
        },
        # [...] Multi account case
    ]
    """
    return __fetch("/map/locations/player")

def getAbilityTree(className:Union["warrior","archer","mage","assassin","shaman"]) -> dict:
    """
    ## Ability Tree
    Get the archetypes and abilities for a class, sorted by pages.

    Parameters:
    - className (Union["warrior","archer","mage","assassin","shaman"]): The name of the class (non-donor, lowercase)

    Returns:
    {
        "archetypes": {
            "archetypeName": {
                "name": str,
                "description": str,
                "shortDescription": str, # Description shown on the AT Gui in game
                "icon": str, # Minecraft legacy item id e.g. 275:67
                "slot": int
            },
            # [...]
        },
        "pages": {
            "pageNumber": {
                "abilityId": {
                    "name": str,
                    "icon": str, # Minecraft legacy item id e.g. 275:67
                    "slot": int,
                    "coordinates": {
                    "x": int,
                    "y": int
                    },
                    "description": [
                        "line1",
                        "line2",
                        # [...]
                    ],
                    "requirements": {
                        "ABILITY_POINTS": int,
                        "NODE": str, # Ability ID of the required node
                        "ARCHETYPE": {
                            "name": str,
                            "amount": int # Number of abilities required in the said archetype
                        },
                    },
                    "links": [ # List of linked abilities, in map this is referred as "family"
                        "abilityId",
                        # [...]
                    ],
                    "locks": [ # List of abilities locking unlock of this one
                        "abilityId",
                        # [...]
                    ],
                    "page": int
                },
                # [...]
            },
            # [...]
        }
    }
    """
    return __fetch(f"/ability/tree/{className}")

def getAbilityMap(className:Union["warrior","archer","mage","assassin","shaman"]) -> dict:
    """
    ## Ability Map
    Get the abilities of a class in a list.

    Parameters:
    - className (Union["warrior","archer","mage","assassin","shaman"]): The name of the class (non-donor, lowercase)

    Returns:
    {
        "pages": int,
        "map": [
            {
                "type": "ability",
                "coordinates": {
                    "x": int,
                    "y": int
                },
                "meta": {
                    "icon": str,  # Minecraft legacy item id e.g. 275:67
                    "page": int,
                   "id": str  # Internal id of the ability, abilities in AT response are refered by the same id
                },
                "familiy": [  # Ability ids listed here are abilities connected to the current one
                    "ability1"
                    # [...]
                ]
            },
            {
                "type": "connector",
                "coordinates": {
                    "x": int,
                    "y": int
                },
                "meta": {
                    "icon": "connector_up_down",
                    # Connector icon syntax is both direction clockwise like right_left or right_down_left
                    "page": int
                },
                "family": [  # Ability ids listed here are abilities assiciated to this connector
                    "ability1",
                    # [...]
                ]
            },
            # [...]
        ]
    }
    """
    return __fetch(f"/ability/map/{className}")

def getLeaderboard(type:Union["guildLevel","guildTerritories","guildWars","combatGlobalLevel","totalGlobalLevel","combatSoloLevel","totalSoloLevel","playerContent","woodcuttingLevel","professionsSoloLevel","miningLevel","fishingLevel","farmingLevel","alchemismLevel","armouringLevel","cookingLevel","jewelingLevel","scribingLevel","tailoringLevel","weaponsmithingLevel","woodworkingLevel","professionsGlobalLevel","nogCompletion","tccCompletion","nolCompletion","tnaCompletion","warsCompletion","ironmanContent","ultimateIronmanContent","craftsmanContent","hardcoreLegacyLevel","huntedContent","hardcoreContent","huicContent","huichContent"], resultLimit:int=100) -> dict:
    """
    ## Leaderboard
    https://wynncraft.com/stats/

    Parameters:
    - type (Union["guildLevel","guildTerritories","guildWars","combatGlobalLevel","totalGlobalLevel","combatSoloLevel","totalSoloLevel","playerContent","woodcuttingLevel","professionsSoloLevel","miningLevel","fishingLevel","farmingLevel","alchemismLevel","armouringLevel","cookingLevel","jewelingLevel","scribingLevel","tailoringLevel","weaponsmithingLevel","woodworkingLevel","professionsGlobalLevel","nogCompletion","tccCompletion","nolCompletion","tnaCompletion","warsCompletion","ironmanContent","ultimateIronmanContent","craftsmanContent","hardcoreLegacyLevel","huntedContent","hardcoreContent","huicContent","huichContent"]): The type of the leaderboard (see before)
    - resultLimit (int): Result limit (default is 100)

    Returns:
    # Guild Leaderboards
    {
        "1": {
            "uuid": str,
            "name": str,
            "prefix": str,
            "xp": int,
            "territories": int,
            "wars": int,
            "level": int,
            "members": int,
            "created": str,
            "banner": {
                "base": str,
                "tier": int,
                "structure": str,
                "layers": [
                    {
                        "colour": str,
                        "pattern": str
                    },
                    # [...]
                ]
            },
        },
        # [...]
    }

    # Player Leaderboards
    {
        "1": {
            "name": str,
            "uuid": str,
            "rank": str,
            "score": int,
            "metadata": {
                "xp": int,
                "playtime": int
            },
            "rankBadge": str,
            "supportRank": str,
            "shortenedRank": str,
            "legacyRankColor": {
                "sub": str,
                "main": str
            },
            "characterType": str,
            "characterUuid": str,
        },
        # [...]
    }

    # Gamemodes leaderboards
    {
        "1": {
            "name": str,
            "uuid": str,
            "rank": str,
            "score": int,
            "metadata": {
                "xp": int,
                "playtime": int
            },
            "rankBadge": str,
            "supportRank": str,
            "shortenedRank": str,
            "legacyRankColor": {
                "sub": str,
                "main": str
            },
            "characterType": str,
            "characterUuid": str,
        },
        # [...]
    }
    """
    return __fetch(f"/leaderboards/{type}?resultLimit={resultLimit}")

def search(query:str) -> dict:
    """
    ## Search
    Search for everything! Players, guilds, items...

    Parameters:
    - query (str): Name
    """
    return __fetch(f"/search/{query}")

def getItemDB(paginated:bool) -> dict:
    """
    ## Item Database
    Get all items.

    Parameters:
    - paginated (bool): Enable pagination or not
    """
    if paginated:
        return __fetch("/item/database")
    else:
        return __fetch("/item/database?fullResult")
def getItemMetadata() -> dict:
    """
    ## Item Metadata
    Get all metadata (like identifications, major IDs, etc...) about items currently ingame
    """
    return __fetch("/item/metadata")

def searchItem(query:str, type:str or list=None, tier:str or int or list=None, attackSpeed:str or list=None, levelRange:int or list=None, professions:str or list=None, identifications:str or list=None, majorIds:str or list=None, paginated:bool=False) -> dict:
    """
    ## Item Search
    Search for all kinds of items with different parameters. Put null to the parameters don't wanna use.
    You can use the getItemMetadata() function to get all metadata you can use for the parameters.

    Parameters:
    - query (str): The name of the item
    - type (str or list): The item's type
    - tier (str or int or list): The item's tier (if ingredient) or rarity (if gear)
    - attackSpeed (str or list): The item's attack speed (if weapon)
    - levelRange (int or list): The item's level range
    - professions (str or list): What professions use the item (if ingredient)
    - identifications (str or list): What identifications the item has
    - majorIds (str or list): What major IDs the item has (if gear)
    - paginated (bool): Enable pagination or not
    """
    requestData = {"query":query}
    if type is not None: requestData["type"] = type
    if tier is not None: requestData["tier"] = tier
    if attackSpeed is not None: requestData["attackSpeed"] = attackSpeed
    if levelRange is not None: requestData["levelRange"] = levelRange
    if professions is not None: requestData["professions"] = professions
    if identifications is not None: requestData["identifications"] = identifications
    if majorIds is not None: requestData["majorIds"] = majorIds

    conn = http.client.HTTPSConnection("api.wynncraft.com")
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(requestData)

    if paginated == True: conn.request("POST", "/v3/item/search?fullResult", body=payload, headers=headers)
    else: conn.request("POST", "/v3/item/search", body=payload, headers=headers)
    res = conn.getresponse()

    responseData = res.read().decode("utf-8")
    conn.close()

    return json.loads(responseData)