function fetch(path) {
    return new Promise((resolve, reject) => {
        const req = require('https').request(`https://api.wynncraft.com/v3${path}`, { method: 'GET' }, (res) => {
            let responseData = '';

            res.on('data', (chunk) => {
                responseData += chunk;
            });

            res.on('end', () => {
                resolve(JSON.parse(responseData));
            });
        })

        req.on('error', (err) => {
            throw err;
        });

        req.end();
    });
}
async function getPlayer(username, uuid, fullStats=false) {
    if ((username !== undefined && uuid === undefined) || (username === undefined && uuid !== undefined)) {
        if (fullStats) {
            return await fetch(`/player/${username||uuid}?fullResult`);
        } else {
            return await fetch(`/player/${username||uuid}`);
        }
    } else {
        throw new TypeError('Invalid parameters provided: Either username or uuid is required');
    }
}
async function getPlayerCharacterList(username, uuid) {
    if ((username !== undefined && uuid === undefined) || (username === undefined && uuid !== undefined)) {
        return await fetch(`/player/${username||uuid}/characters`);
    } else {
        throw new TypeError('Invalid parameters provided: Either username or uuid is required');
    }
}
async function getPlayerCharacter(username, uuid, characterUUID) {
    if ((username !== undefined && uuid === undefined) || (username === undefined && uuid !== undefined)) {
        return await fetch(`/player/${username||uuid}/characters/${characterUUID}`);
    } else {
        throw new TypeError('Invalid parameters provided: Either username or uuid is required');
    }
}
async function getPlayerCharacterAbilityMap(username, uuid, characterUUID) {
    if ((username !== undefined && uuid === undefined) || (username === undefined && uuid !== undefined)) {
        return await fetch(`/player/${username||uuid}/characters/${characterUUID}/abilities`);
    } else {
        throw new TypeError('Invalid parameters provided: Either username or uuid is required');
    }
}
async function getOnlinePlayers(identifier, server) {
    return await fetch(`/player?identifier=${identifier}&server=${server}`);
}
async function getGuild(name, prefix, identifier) {
    if ((name !== undefined && prefix === undefined) || (name === undefined && prefix !== undefined)) {
        if (prefix) {
            return await fetch(`/guild/prefix/${prefix}?identifier=${identifier}`);
        } else {
            return await fetch(`/guild/${name}?identifier=${identifier}`);
        }
    } else {
        throw new TypeError('Invalid parameters provided: Either name or prefix is required');
    }
}
async function getGuildsList(identifier) {
    return await fetch(`/guild/list/guild?identifier=${identifier}`);
}
async function getTerritoryList() {
    return await fetch(`/guild/list/territory`);
}
async function getNews() {
    return await fetch('/latest-news');
}
async function getClasses() {
    return await fetch('/classes');
}
async function getClassInfo(className) {
    return await fetch(`/classes/${className}`);
}
async function getQuestsCount() {
    return await fetch(`/map/quests`);
}
async function getMapLocations() {
    return await fetch(`/map/locations/markers`);
}
async function getPlayerLocations() {
    return await fetch(`/map/locations/player`);
}
async function getAbilityTree(className) {
    return await fetch(`/ability/tree/${className}`);
}
async function getAbilityMap(className) {
    return await fetch(`/ability/map/${className}`);
}
async function getLeaderboard(type, resultLimit=100) {
    return await fetch(`/leaderboards/${type}?resultLimit=${resultLimit}`);
}
async function search(query) {
    return await fetch(`/search/${query}`);
}
async function getItemDB(paginated) {
    if (paginated) {
        return await fetch(`/item/database`);
    } else {
        return await fetch(`/item/database?fullResult`);
    }
}
async function searchItem(query) {
    return await fetch(`/item/search/${query}`);
}
async function getItemMetadata() {
    return await fetch(`/item/metadata`);
}
async function searchItem(query, type, tier, attackSpeed, levelRange, professions, identifications, majorIds) {
    return await new Promise((resolve, reject) => {
        const req = require('https').request(`https://api.wynncraft.com/v3/item/search`, { method: 'POST', headers: {"Content-Type":"application/json"} }, (res) => {
            let responseData = '';

            res.on('data', (chunk) => {
                responseData += chunk;
            });

            res.on('end', () => {
                resolve(JSON.parse(responseData));
            });
        })

        req.on('error', (err) => {
            throw err;
        });

        const requestData = {};

        if (query !== null) requestData.query = query;
        if (type !== null) requestData.type = type;
        if (tier !== null) requestData.tier = tier;
        if (attackSpeed !== null) requestData.attackSpeed = attackSpeed;
        if (levelRange !== null) requestData.levelRange = levelRange;
        if (professions !== null) requestData.professions = professions;
        if (identifications !== null) requestData.identifications = identifications;
        if (majorIds !== null) requestData.majorIds = majorIds;

        req.write(JSON.stringify(requestData));
        req.end();
    });
}
module.exports = {
    getPlayer,
    getPlayerCharacterList,
    getPlayerCharacter,
    getPlayerCharacterAbilityMap,
    getOnlinePlayers,
    getGuild,
    getGuildsList,
    getTerritoryList,
    getNews,
    getClasses,
    getClassInfo,
    getQuestsCount,
    getMapLocations,
    getPlayerLocations,
    getAbilityTree,
    getAbilityMap,
    getLeaderboard,
    search,
    getItemDB,
    searchItem,
    getItemMetadata,
};