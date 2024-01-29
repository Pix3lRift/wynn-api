/**
 * ## Player Info
 * Get all kind of information about a player.
 * Use either username or uuid, put unidentified to the one you're not using
 * @param username - Username of the player
 * @param uuid - UUID of the player
 * @param fullStats - When true, get all characters (classes) of the player too.
 */
export function getPlayer(username?:string, uuid?:string, fullStats: boolean): Promise<{"username":string,"online":boolean,"server":string|null,"activeCharacter":string|null,"uuid":string,"rank":string,"rankBadge":string,"legacyRankColour":{"main":string,"sub":string},"shortenedRank":string|null,"supportRank":string,"veteran":boolean,"firstJoin":string,"lastJoin":string,"playtime":Number,"guild":{"name":string,"prefix":string,"rank":string,"rankStars":string},"globalData":{"wars":Number,"totalLevels":Number,"killedMobs":Number,"chestsFound":Number,"dungeons":{"total":Number,"list":Object},"raids":{"total":Number,"list":Object},"completedQuests":Number,"pvp":{"kills":Number,"deaths":Number}},"forumLink":Number|null,"ranking":Object,"publicProfile":boolean,"characters"?:Object}>
/**
 * Get all kind of information about a player's character (class).
 * Use either username or uuid, put unidentified to the one you're not using
 * @param username - Username of the player
 * @param uuid - UUID of the player
 * @param characterUUID - The player's character's UUID (get by using {@link getPlayerCharacterList()})
 */
export function getPlayerCharacter(username?:string, uuid?:string, characterUUID: string): Promise<{"type":string,"nickname":string|null,"level":Number,"xp":Number,"xpPercent":Number,"totalLevel":Number,"wars":Number,"playtime":Number,"mobsKilled":Number,"chestsFound":Number,"blocksWalked":Number,"itemsIdentified":Number,"logins":Number,"deaths":Number,"discoveries":Number,"pvp":{"kills":Number,"deaths":Number},"gamemode":Array,"skillPoints":{"strength":Number,"dexterity":Number,"intelligence":Number,"defence":Number,"agility":Number}|{},"professions":{"fishing":{"level":Number,"xpPercent":Number},"woodcutting":{"level":Number,"xpPercent":Number},"mining":{"level":Number,"xpPercent":Number},"farming":{"level":Number,"xpPercent":Number},"scribing":{"level":Number,"xpPercent":Number},"jeweling":{"level":Number,"xpPercent":Number},"alchemism":{"level":Number,"xpPercent":Number},"cooking":{"level":Number,"xpPercent":Number},"weaponsmithing":{"level":Number,"xpPercent":Number},"tailoring":{"level":Number,"xpPercent":Number},"woodworking":{"level":Number,"xpPercent":Number},"armouring":{"level":Number,"xpPercent":Number}},"dungeons":{"total":Number,"list":Object|null},"raids":{"total":Number,"list":Object}|null,"quests":Array<string>}>
/**
 * ## Character List
 * Get a player's character (class) list.
 * Use either username or uuid, put unidentified to the one you're not using
 * @param username - Username of the player
 * @param uuid - UUID of the player
 */
export function getPlayerCharacterList(username?:string, uuid?:string): Promise<Object>;
/**
 * ## Player's Ability Map
 * Get a player's ability map on a specific character.
 * Use either username or uuid, put unidentified to the one you're not using.
 * @param username - Username of the player
 * @param uuid - UUID of the player
 * @param characterUUID - The player's character's UUID (get by using {@link getPlayerCharacterList()})
 */
export function getPlayerCharacterAbilityMap(username?:string, uuid?:string, characterUUID: string): Promise<{"pages":Number,"map":Array<{"type":"ability"|"connector","coordinates":{"x":Number,"y":Number},"meta":{"icon":string,"page":Number,"id"?:string},"family":Array<string>}>}>;
/**
 * ## Online Players
 * Get currently online players (on specific servers).
 * @param identifier - How players should be identified (by name or by UUID)
 * @param server - Format: "WC1" or 1 or ["WC1", "2"]
 */
export function getOnlinePlayers(identifier:"username"|"uuid", server:string|Array<Number>|Array<string>): Promise<{"onlinePlayers":Number,"players":Object}>;
/**
 * ## Guild Info
 * Use either name or prefix, put unidentified to the one you're not using.
 * @param name - The name of the guild
 * @param prefix - Prefix of the guild
 * @param identifier - How players should be identified (by name or by UUID)
 */
export function getGuild(name?:string, prefix?:string, identifier:"username"|"uuid"): Promise<{"uuid":string,"name":string,"prefix":string,"level":Number,"xpPercent":Number,"territories":Number,"wars":Number,"created":string,"members":{"total":Number,"owner":Object,"chief":Object,"strategist":Object,"captain":Object,"recruiter":Object,"recruit":Object},"online":Number,"banner":{"base":string,"tier":Number,"structure":string,"layers":Array<{"colour":string,"pattern":string}>},"seasonRanks":Object}>;
/**
 * ## Guild List
 * Get all existing guilds.
 * @param identifier - See https://documentation.wynncraft.com/docs/modules/guild.html#guild-list
 */
export function getGuildsList(identifier:"name"|"uuid"): Promise<Object>;
/**
 * ## Territories
 * Get a list of all territories and their infos (the guild currently owning it, when it was acquired and its location).
 */
export function getTerritoryList(): Promise<Object>;
/**
 * ## News
 * Get the latest news about wynncraft.
 */
export function getNews(): Promise<Array<{"title":string,"date":string,"forumThread":string,"author":string,"content":string,"comments":string}>>;
/**
 * ## Classes
 * Get all classes with thier overall difficulty.
 */
export function getClasses(): Promise<Object>;
/**
 * ## Class Info
 * Get infos about a class (like ID, name, lore, etc...).
 * @param className - The name of the class (non-donor, lowercase)
 */
export function getClassInfo(className:"warrior"|"archer"|"mage"|"assassin"|"shaman"): Promise<{"id":string,"name":string,"lore":string,"overallDifficulty":Number,"archetypes":Object}>;
/**
 * ## Quests
 * Get the count of quests (including mini-quests).
 */
export function getQuestsCount(): Promise<{"quests":Number}>;
/**
 * ## Map Locations
 * Get all markers on the map. https://map.wynncraft.com/
 */
export function getMapLocations(): Promise<Array<{"name":string,"icon":string,"x":Number,"y":Number,"z":Number}>>;
/**
 * ## Players on the map
 * Get all players (yourself, friends, party members, guild members) on the map. https://map.wynncraft.com/
 */
export function getPlayerLocations(): Promise<Array<{"uuid":string,"name":string,"nickname":string,"server":string,"x":Number,"y":Number,"z":Number,"friends":Array<{"uuid":string,"name":string,"nickname":string,"server":string,"x":Number,"y":Number,"z":Number}>,"party":Array<{"uuid":string,"name":string,"nickname":string,"server":string,"x":Number,"y":Number,"z":Number}>,"guild":Array<{"uuid":string,"name":string,"nickname":string,"server":string,"x":Number,"y":Number,"z":Number}>}>>;
/**
 * ## Ability Tree
 * Get the archetypes and abilities for a class, sorted by pages.
 * @param className - The name of the class (non-donor, lowercase)
 */
export function getAbilityTree(className:"warrior"|"archer"|"mage"|"assassin"|"shaman"): Promise<{"archetypes":Object,"pages":Object}>;
/**
 * ## Ability Map
 * Get the abilities of a class in an Array.
 * @param className - The name of the class (non-donor, lowercase)
 */
export function getAbilityMap(className:"warrior"|"archer"|"mage"|"assassin"|"shaman"): Promise<{"pages":Number,"map":Array<{"type":"ability"|"connector","coordinates":{"x":Number,"y":Number},"meta":{"icon":string,"page":Number,"id"?:string},"family":Array<string>}>}>;
/**
 * ## Leaderboard
 * https://wynncraft.com/stats/
 * @param type - The type of the leaderboard (see the typings)
 * @param resultLimit - Result limit (default is 100)
 */
export function getLeaderboard(type:"guildLevel"|"guildTerritories"|"guildWars"|"combatGlobalLevel"|"totalGlobalLevel"|"combatSoloLevel"|"totalSoloLevel"|"playerContent"|"woodcuttingLevel"|"professionsSoloLevel"|"miningLevel"|"fishingLevel"|"farmingLevel"|"alchemismLevel"|"armouringLevel"|"cookingLevel"|"jewelingLevel"|"scribingLevel"|"tailoringLevel"|"weaponsmithingLevel"|"woodworkingLevel"|"professionsGlobalLevel"|"nogCompletion"|"tccCompletion"|"nolCompletion"|"tnaCompletion"|"warsCompletion"|"ironmanContent"|"ultimateIronmanContent"|"craftsmanContent"|"hardcoreLegacyLevel"|"huntedContent"|"hardcoreContent"|"huicContent"|"huichContent",resultLimit:Number=100): Promise<Object>
/**
 * ## Search
 * Search for everything! Players, guilds, items...
 * @param query - Name
 */
export function search(query:string): Promise<{"query":string,"players":Object,"guilds":Object,"guildsPrefix":Object,"territories":Object,"discoveries":Object,"items":Object}>;
/**
 * ## Item Database
 * Get all items.
 * @param paginated - Enable pagination or not
 */
export function getItemDB(paginated:boolean): Promise<Object>;
/**
 * ## Item Search (lite)
 * Search for all kinds of items.
 * @param query - The name of the item
 */
export function searchItem(query:string): Promise<Object>;
/**
 * ## Item Metadata
 * Get all metadata (like identifications, major IDs, etc...) about items currently ingame
 */
export function getItemMetadata(): Promise<Object>;
/**
 * ## Item Search
 * Search for all kinds of items with different parameters. Put null to the parameters don't wanna use.
 * You can use the {@link getItemMetadata()} function to get all metadata you can use for the parameters.
 * @param query - The name of the item
 * @param type - The item's type
 * @param tier - The item's tier (if ingredient) or rarity (if gear)
 * @param attackSpeed The item's attack speed (if weapon)
 * @param levelRange - The item's level range
 * @param professions - What professions use the item (if ingredient)
 * @param identifications - What identifications the item has
 * @param majorIds - What major IDs the item has (if gear)
 */
export function searchItem(query?:string,type?:string|Array<string>,tier?:Number|Array<Number>|string|Array<string>,attackSpeed?:string|Array<string>,levelRange?:Number|Array<Number>,professions?:string|Array<string>,identifications?:string|Array<string>,majorIds?:string|Array<string>): Promise<Object>;