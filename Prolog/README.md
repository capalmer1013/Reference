# Prolog Notes

---

## Getting Started

- obviously install swipl (now available on fedora :)
- **Knowledge Base** - compiled file of collection of facts
- **Facts** - used to state things that are unconditionally true of some situation of interest.
example:
```prolog
woman(mia).
woman(jody).
woman(yolanda).
playsAirGuitar(jody).
party.
```
states that: Mia, Jody, and Yolanda are women, Jody plays air guitar, and that a party is taking place.

- *opening a file* - `?- consult('FILEPATH').

- *shorthand version* - `['FILEPATH'].`

- *loading file from launch* - `prolog -s FILENAME.pl`

- *exit swipl* - `halt.`


test.pl:
```prolog
human(john).
```
swipl:
```
?- ['test.pl']
% test.pl compiled 0.00 sec, 2 clauses
true.

?- human(john).
true.

?- human(Who).
Who = john.

?- halt.
```
