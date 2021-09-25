#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:14:01 2021

@author: stuart
"""

#combine grimdark firefight rules

import os
from PyPDF4 import PdfFileMerger

def cleanGDFFFilename(name):
    
    cleanName = name.split(' - ')[-1]
    cleanName = cleanName.split(' v')[0]
    
    return cleanName

###################################
### End of function definitions ###
###################################

baseFolder = './rules/grimdarkFutureFirefightRules'

armyListFolder = os.path.join(baseFolder, 'armyLists')


armyListFiles = ['GFF - Battle Brothers v2.13.pdf',
              'GFF - Battle Brother Detachments v2.15.pdf',
              'GFF - Prime Brothers v2.15.pdf',
              'GFF - Human Defense Force v2.13.pdf',
              'GFF - Rebel Guerrillas v2.6.pdf',
              'GFF - Feudal Guard v2.9.pdf',
              'GFF - Battle Sisters v2.11.pdf',
              'GFF - Custodian Brothers v2.2.pdf',
              'GFF - Human Inquisition v2.8.pdf',
              'GFF - Gangs of Hive City v2.5.pdf',
              'GFF - Machine Cult v2.11.pdf',
              'GFF - Havoc Brothers v2.12.pdf',
              'GFF - Havoc Brother Disciples v2.18.pdf',
              'GFF - Infected Colonies v2.5.pdf',
              'GFF - Machine Cult Defilers v2.6.pdf',
              'GFF - Wormhole Daemons v2.9.pdf',
              'GFF - High Elf Fleets v2.9.pdf',
              'GFF - Elven Jesters v2.7.pdf',
              'GFF - Dark Elf Raiders v2.7.pdf',
              'GFF - Alien Hives v2.11.pdf',
              'GFF - Soul-Snatcher Cults v2.9.pdf',
              'GFF - Dwarf Guilds v2.7.pdf',
              'GFF - Ratmen Clans v2.6.pdf',
              'GFF - Vile Rattus Cult v2.6.pdf',
              'GFF - Robot Legions v2.17.pdf',
              'GFF - Orc Marauders v2.14.pdf',
              'GFF - TAO Coalition v2.11.pdf']


#build the joint army list
armyListMerger = PdfFileMerger(strict=False)

for armyListFilename in armyListFiles:
    armyListName = armyListFilename.split(' - ')[-1]
    armyListName = armyListName.split(' v')[0]
    
    armyListName = cleanGDFFFilename(armyListFilename)
    
    loadName = os.path.join(armyListFolder, armyListFilename)
    
    armyListMerger.append(fileobj=open(loadName, 'rb'), bookmark = armyListName)
    
armyListMerger.write(fileobj=open('GDFF_armyLists.pdf', 'wb'))
armyListMerger.close()

# create GDFF full rules
armyListFiles.insert(0, 'GFF - Basic Rulebook v2.12.pdf')
    
allMerger = PdfFileMerger(strict=False)
for fi, filename in enumerate(armyListFiles):
    
    if fi == 0:
        bookmark = filename.split(' v')[0]
        allMerger.append(fileobj = open(os.path.join(baseFolder, filename), 'rb'), bookmark = bookmark)
        
    else:
        bookmark = cleanGDFFFilename(filename)
        allMerger.append(fileobj = open(os.path.join(armyListFolder, filename), 'rb'), bookmark = bookmark)
    
allMerger.write(fileobj = open('GDFF_full_rules.pdf', 'wb'))
allMerger.close()
