# sublime-fillstruct
golang fillstruct for sublime text

> Place the **cursor between the curly braces** for a correct autofill.
> This should sync with autocomplete cursor positioning

![gif](https://raw.githubusercontent.com/twoojoo/sublime-fillstruct/main/fillstruct.gif)

## install

```bash
go install github.com/davidrjenni/reftools/cmd/fillstruct@latest

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
