#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:37:57 2021

@author: stuart
"""

#combine grim dark future rules


import os
from PyPDF4 import PdfFileMerger

def cleanGDFFFilename(name):
    
    cleanName = name.split(' - ')[-1]
    cleanName = cleanName.split(' v')[0]
    
    return cleanName

###################################
### End of function definitions ###
###################################

baseFolder = './rules/grimdarkFutureRules'

armyListFolder = os.path.join(baseFolder, 'armyLists')

#build the armyList
armyListFiles = ['GF - Battle Brothers v2.13.pdf',
              'GF - Battle Brother Detachments v2.15.pdf',
              'GF - Prime Brothers v2.15.pdf',
              'GF - Human Defense Force v2.13.pdf',
              'GF - Rebel Guerrillas v2.6.pdf',
              'GF - Feudal Guard v2.9.pdf',
              'GF - Battle Sisters v2.11.pdf',
              'GF - Custodian Brothers v2.2.pdf',
              'GF - Human Inquisition v2.8.pdf',
              'GF - Machine Cult v2.11.pdf',
              'GF - Havoc Brothers v2.12.pdf',
              'GF - Havoc Brother Disciples v2.18.pdf',
              'GF - Infected Colonies v2.5.pdf',
              'GF - Machine Cult Defilers v2.6.pdf',
              'GF - Wormhole Daemons v2.9.pdf',
              'GF - High Elf Fleets v2.10.pdf',
              'GF - Elven Jesters v2.7.pdf',
              'GF - Dark Elf Raiders v2.7.pdf',
              'GF - Alien Hives v2.13.pdf',
              'GF - Soul-Snatcher Cults v2.9.pdf',
              'GF - Dwarf Guilds v2.7.pdf',
              'GF - Ratmen Clans v2.6.pdf',
              'GF - Vile Rattus Cult v2.6.pdf',
              'GF - Robot Legions v2.19.pdf',
              'GF - Orc Marauders v2.14.pdf',
              'GF - TAO Coalition v2.11.pdf']


#build the joint army list
armyListMerger = PdfFileMerger(strict=False)

for armyListFilename in armyListFiles:
    armyListName = armyListFilename.split(' - ')[-1]
    armyListName = armyListName.split(' v')[0]
    
    armyListName = cleanGDFFFilename(armyListFilename)
    
    loadName = os.path.join(armyListFolder, armyListFilename)
    
    armyListMerger.append(fileobj=open(loadName, 'rb'), bookmark = armyListName)
    
armyListMerger.write(fileobj=open('GDF_armyLists.pdf', 'wb'))
armyListMerger.close()

# create GDF full rules
armyListFiles.insert(0, 'GF - Basic Rulebook v2.12.pdf')
    
allMerger = PdfFileMerger(strict=False)
for fi, filename in enumerate(armyListFiles):
    
    if fi == 0:
        bookmark = filename.split(' v')[0]
        allMerger.append(fileobj = open(os.path.join(baseFolder, filename), 'rb'), bookmark = bookmark)
        
    else:
        bookmark = cleanGDFFFilename(filename)
        allMerger.append(fileobj = open(os.path.join(armyListFolder, filename), 'rb'), bookmark = bookmark)
    
allMerger.write(fileobj = open('GDF_full_rules.pdf', 'wb'))
allMerger.close()