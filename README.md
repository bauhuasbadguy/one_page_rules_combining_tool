# One page rules combining tool

## Introduction

This is a couple of scripts I quickly dashed off to combine the one page rules army lists and core rules into a single pdf I could send to people who were vaguely interested but didn't want to go digging. Each script combines the core rules and army lists as of 25/09/21, any more updates to the rules versions will cause crashes but it should be trivial to update the version numbers.

## Usage

Each of the scripts is pretty simple. You should be able to just run it. The expected folder structure is shown below, using the grimdark future rules

```
one_page_rules_combining_tool
├── combineAoF.py
├── combineAoFR.py
├── combineAoFSkirmish.py
├── combineGDFF.py
├── combineGDF.py
├── README.md
└── rules
    └── grimdarkFutureRules
        │   ├── armyLists
        │   │   ├── GF - Alien Hives v2.13.pdf
        │   │   ├── GF - Battle Brother Detachments v2.15.pdf
        │   │   ├── GF - Battle Brothers v2.13.pdf
        │   │   ├── GF - Battle Sisters v2.11.pdf
        │   │   ├── GF - Custodian Brothers v2.2.pdf
        │   │   ├── GF - Dark Elf Raiders v2.7.pdf
        │   │   ├── GF - Dwarf Guilds v2.7.pdf
        │   │   ├── GF - Elven Jesters v2.7.pdf
        │   │   ├── GF - Feudal Guard v2.9.pdf
        │   │   ├── GF - Havoc Brother Disciples v2.18.pdf
        │   │   ├── GF - Havoc Brothers v2.12.pdf
        │   │   ├── GF - High Elf Fleets v2.10.pdf
        │   │   ├── GF - Human Defense Force v2.13.pdf
        │   │   ├── GF - Human Inquisition v2.8.pdf
        │   │   ├── GF - Infected Colonies v2.5.pdf
        │   │   ├── GF - Machine Cult Defilers v2.6.pdf
        │   │   ├── GF - Machine Cult v2.11.pdf
        │   │   ├── GF - Orc Marauders v2.14.pdf
        │   │   ├── GF - Prime Brothers v2.15.pdf
        │   │   ├── GF - Ratmen Clans v2.6.pdf
        │   │   ├── GF - Rebel Guerrillas v2.6.pdf
        │   │   ├── GF - Robot Legions v2.19.pdf
        │   │   ├── GF - Soul-Snatcher Cults v2.9.pdf
        │   │   ├── GF - TAO Coalition v2.11.pdf
        │   │   ├── GF - Titan Lords v2.4.pdf
        │   │   ├── GF - Vile Rattus Cult v2.6.pdf
        │   │   └── GF - Wormhole Daemons v2.9.pdf
        │   ├── GF - Basic Rulebook v2.12.pdf
        │   └── GF - Core Rules v2.12.pdf

```

In this example you would run `combineGDF.py` and it would produce the full army lists and the combined army lists and rules in the folder - `one_page_rules_combining_tool`.

## Requirements

* PyPDF4

## Contact

No
