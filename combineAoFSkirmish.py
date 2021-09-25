#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:48:12 2021

@author: stuart
"""

#age of fantasy skirmish rules combining



import os
from PyPDF4 import PdfFileMerger

def cleanAoFFilename(name):
    
    cleanName = name.split(' - ')[-1]
    cleanName = cleanName.split(' v')[0]
    
    return cleanName

###################################
### End of function definitions ###
###################################

baseFolder = './rules/ageOfFantasySkirmishRules'

armyListFolder = os.path.join(baseFolder, 'armyLists')

#build the armyList
armyListFiles = ['AoFS - Kingdom of Angels v2.4.pdf',
              'AoFS - Eternal Wardens v2.9.pdf',
              'AoFS - Humans v2.6.pdf',
              'AoFS - Chivalrous Kingdoms v2.4.pdf',
              'AoFS - Duchies of Vinci v2.3.pdf',
              'AoFS - Halflings v2.6.pdf',
              'AoFS - Dwarves v2.9.pdf',
              'AoFS - Volcanic Dwarves v2.8.pdf',
              'AoFS - Sky-City Dwarves v2.8.pdf',
              'AoFS - High Elves v2.9.pdf',
              'AoFS - Wood Elves v2.6.pdf',
              'AoFS - Deep-Sea Elves v2.5.pdf',
              'AoFS - Dark Elves v2.7.pdf',
              'AoFS - Saurians v2.7.pdf',
              'AoFS - Ratmen v2.13.pdf',
              'AoFS - Havoc Warriors v2.10.pdf',
              'AoFS - Havoc Warrior Disciples v2.12.pdf',
              'AoFS - Havoc Dwarves v2.2.pdf',
              'AoFS - Shadow Stalkers v2.3.pdf',
              'AoFS - Rift Daemons v2.7.pdf',
              'AoFS - Vampiric Undead v2.11.pdf',
              'AoFS - Mummified Undead v2.12.pdf',
              'AoFS - Ossified Undead v2.3.pdf',
              'AoFS - Ghostly Undead v2.8.pdf',
              'AoFS - Goblins v2.12.pdf',
              'AoFS - Orcs v2.9.pdf',
              'AoFS - Beastmen v2.7.pdf',
              'AoFS - Ogres v2.5.pdf']
    
# build the joint army lists
armyListMerger = PdfFileMerger(strict=False)

for armyListFilename in armyListFiles:
    armyListName = armyListFilename.split(' - ')[-1]
    armyListName = armyListName.split(' v')[0]
    
    armyListName = cleanAoFFilename(armyListFilename)
    
    loadName = os.path.join(armyListFolder, armyListFilename)
    
    armyListMerger.append(fileobj=open(loadName, 'rb'), bookmark = armyListName)
    
armyListMerger.write(fileobj=open('AoFS_armyLists.pdf', 'wb'))
armyListMerger.close()

# create AoFS full rules
armyListFiles.insert(0, 'AoFS - Basic Rulebook v2.12.pdf')
    
allMerger = PdfFileMerger(strict=False)
for fi, filename in enumerate(armyListFiles):
    
    if fi == 0:
        bookmark = filename.split(' v')[0]
        allMerger.append(fileobj = open(os.path.join(baseFolder, filename), 'rb'), bookmark = bookmark)
        
    else:
        bookmark = cleanAoFFilename(filename)
        allMerger.append(fileobj = open(os.path.join(armyListFolder, filename), 'rb'), bookmark = bookmark)
    
allMerger.write(fileobj = open('AoFS_full_rules.pdf', 'wb'))
allMerger.close()