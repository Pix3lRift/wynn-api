(go back to the [Node.js version](https://github.com/Pix3lRift/wynn-api/tree/node-v3))
## About
A simple API wrapper for the [Wynncraft API](https://documentation.wynncraft.com/)

- Dictionary-oriented
- Flexible and powerful
- 100% coverage of the V3 Wynncraft API
## Installation

**Python 3.5 or newer is required.**


```sh
pip install wynn-api
```

## Example Usage
```js
import wynn_api as WynnAPI

salted = WynnAPI.getPlayer("Salted")
```

```js
print(WynnAPI.getPlayer("Salted")["globalData"]["chestsFound"])
```

```js
pfinderSet = WynnAPI.searchItem('Morph')
print(pfinderSet)
```

## Links

- [Github](https://github.com/Pix3lRift/wynn-api/tree/py-v3)
- [Wynncraft Developers discord server](https://discord.gg/CtMKp3hG66)
- [pypi](https://pypi.org/project/wynn-api)
- [npm](https://www.npmjs.com/package/wynn-api-node)
