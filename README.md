## About
A simple API wrapper for the [Wynncraft API](https://documentation.wynncraft.com/)

- Promise based
- Object-oriented
- 100% coverage of the V3 Wynncraft API
## Installation

**Node.js 6.0.0 or newer is required.**


```sh
npm install wynn-api-node
yarn add wynn-api-node
pnpm add wynn-api-node
bun add wynn-api-node
```

## Example Usage
```js
const WynnAPI = require('wynn-api-node');

let salted = await WynnAPI.getPlayer("Salted")
```

```js
WynnAPI.getPlayer("Salted")
.then(player => console.log(player.globalData.chestsFound))
```

```js
let pfinderSet = await WynnAPI.searchItem('Morph')
console.log(pfinderSet)
```

## Links

- [Github](https://github.com/Pix3lRift/wynn-api/)
- [Wynncraft Developers discord server](https://discord.gg/CtMKp3hG66)
- [npm](https://www.npmjs.com/package/wynn-api)