# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:38:56 2018

@author: Nigel
"""
def generateHouseDB():
    houseDatabase = []

    for x in range(1000):
        locationList = ['tampines', 'bukit-timah', 'jurong-east', 'kallang']
        location = locationList[x%4]
        
        typeList = ['4room', '5room', 'EC']
        houseType = typeList[x%3]
        
        house = ['NAME', x*1000, houseType, location]
        houseDatabase.append(house)
        
    return houseDatabase


