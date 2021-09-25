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

baseFolder = './rules/ageOfFantasyRules'

armyListFolder = os.path.join(baseFolder, 'armyLists')

# build the army list
armyListFiles = ['AoF - Kingdom of Angels v2.5.pdf',
              'AoF - Eternal Wardens v2.9.pdf',
              'AoF - Humans v2.9.pdf',
              'AoF - Chivalrous Kingdoms v2.6.pdf',
              'AoF - Duchies of Vinci v2.3.pdf',
              'AoF - Halflings v2.6.pdf',
              'AoF - Dwarves v2.11.pdf',
              'AoF - Volcanic Dwarves v2.9.pdf',
              'AoF - Sky-City Dwarves v2.8.pdf',
              'AoF - High Elves v2.9.pdf',
              'AoF - Wood Elves v2.8.pdf',
              'AoF - Deep-Sea Elves v2.6.pdf',
              'AoF - Dark Elves v2.7.pdf',
              'AoF - Saurians v2.8.pdf',
              'AoF - Ratmen v2.13.pdf',
              'AoF - Havoc Warriors v2.11.pdf',
              'AoF - Havoc Warrior Disciples v2.12.pdf',
              'AoF - Havoc Dwarves v2.3.pdf',
              'AoF - Shadow Stalkers v2.4.pdf',
              'AoF - Rift Daemons v2.9.pdf',
              'AoF - Vampiric Undead v2.12.pdf',
              'AoF - Mummified Undead v2.13.pdf',
              'AoF - Ossified Undead v2.4.pdf',
              'AoF - Ghostly Undead v2.9.pdf',
              'AoF - Goblins v2.12.pdf',
              'AoF - Orcs v2.9.pdf',
              'AoF - Beastmen v2.8.pdf',
              'AoF - Ogres v2.6.pdf',
              'AoF - Giant Tribes v2.0.pdf']
    
# build the joint army list
armyListMerger = PdfFileMerger(strict=False)

for armyListFilename in armyListFiles:
    armyListName = armyListFilename.split(' - ')[-1]
    armyListName = armyListName.split(' v')[0]
    
    armyListName = cleanAoFFilename(armyListFilename)
    
    loadName = os.path.join(armyListFolder, armyListFilename)
    
    armyListMerger.append(fileobj=open(loadName, 'rb'), bookmark = armyListName)
    
armyListMerger.write(fileobj=open('AoF_armyLists.pdf', 'wb'))
armyListMerger.close()

# create GDFF full rules
armyListFiles.insert(0, 'AoF - Basic Rulebook v2.12.pdf')
    
allMerger = PdfFileMerger(strict=False)
for fi, filename in enumerate(armyListFiles):
    
    if fi == 0:
        bookmark = filename.split(' v')[0]
        allMerger.append(fileobj = open(os.path.join(baseFolder, filename), 'rb'), bookmark = bookmark)
        
    else:
        bookmark = cleanAoFFilename(filename)
        allMerger.append(fileobj = open(os.path.join(armyListFolder, filename), 'rb'), bookmark = bookmark)
    
allMerger.write(fileobj = open('AoF_full_rules.pdf', 'wb'))
allMerger.close()