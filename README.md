# sublime-fillstruct
golang fillstruct for sublime text

> place the **cursor between the curly braces** for a correct autofill
> should sync with autocomplete cursor positioning

## install

```bash
git clone git@github.com:twoojoo/sublime-fillstruct.git
cp ./fillstruct.py ~/.config/sublime-text/Packages/User
```

## kebinding

Just add the commad to your keybindings
```json5
[
  //...
  {"keys": ["ctrl+alt+f"], "command": "fillstruct"},
  //...
]
```
