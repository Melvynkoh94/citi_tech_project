# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 20:25:16 2018

@author: Nigel
"""
import re
import urllib.request, urllib.parse, urllib.error

url = 'https://stackedhomes.com/hdb-estates.html'

fhand = urllib.request.urlopen(url)
web = fhand.read().decode()
#print(web)

# Extract list of estates on website
estateList = []
estates = re.findall('<div id="(.*?)"></div>', web)
for item in estates:
    item = item.capitalize()
    item = '-'.join([word.capitalize() for word in item.split('-')])    #'Ang-mo-kio' --> 'Ang-Mo-Kio' 
    estateList.append(item)
estateList = estateList[1:]

# Extract list of estate types on website
estateTypeList = []
estateType = re.findall('<p>(.*? Estate)</p>', web)
for item in estateType:
    estateTypeList.append(item)

#print(estateList, estateTypeList)

#print(len(estateList),len(estateTypeList))

# Dict of estate: estate type
estateDict = {}
for x in range(len(estateList)):
    estateDict[estateList[x]] = estateTypeList[x]

print('estateDict: ')
print(estateDict)
print()
print('estateList: ')
print(estateList)


def generateEstateList():
    print(estateList)
    return estateList


file = open('estateList.txt', 'w+')
for x in range(len(estateList)):
    file.write(estateList[x] + '|' + estateTypeList[x])
    file.write('\n')


"""
def main():
    generateEstateList()

if __name__ == '__main__':
    main()
"""