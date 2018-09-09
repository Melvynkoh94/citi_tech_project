# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:26:52 2018

@author: Nigel
"""
import numpy as np

class Buyer:
    firstTimeOwner = 1
    proximityFromParents = 1
    worked12Months = 1
    housingType = ''
    
    def __init__(self, age, gender, monthlyIncome, expenses, personalSavings, availDownPay, existingLoan, propertyLocation):
        self.age = age
        self.gender = gender
        self.monthlyIncome = monthlyIncome
        self.expenses = expenses
        self.personalSavings = personalSavings
        self.availDownPay = availDownPay
        self.existingLoan = existingLoan
        self.propertyLocation = propertyLocation
    
    def setHousingType(self, housingType):
        self.housingType = housingType
        return
        
    def notFirstTimeOwner(self):
        self.firstTimeOwner = 0
        return
    
    def notNearParents(self):
        self.proximityFromParents = 0
        return
    
    def notWorked12Months(self):
        self.worked12Months = 0
        return
    
    def AHGAmount(self):
        # Returns additional CPF housing grant values, if any
        
        # Checks eligibility
        if self.firstTimeOwner == 0:
            return 0
        if self.monthlyIncome > 5000:
            return 0
        if self.worked12Months == 0:
            return 0
        if self.housingType == 'EC':
            return 0
        
        AHGDict = {
                1500: 40000,
                2000: 35000,
                2500: 30000,
                3000: 25000,
                3500: 20000,
                4000: 15000,
                4500: 10000,
                5000: 50000
                }
        # Info from https://dollarsandsense.sg/complete-guide-to-hdb-housing-grants-in-singapore-for-different-types-of-flats/
        
        for incomeCeiling in AHGDict:
            if self.monthlyIncome <= incomeCeiling:
                AHGValue = AHGDict[incomeCeiling]
                break
        return AHGValue
    
    def SHGAmount(self):
        # Returns special CPF housing grant values, if any    
        
        # Import the web scraper to obtain types of estates for various locations
        # import EstateTypeScraper
        # estateTypeDict = EstateTypeScraper.estateDict
        
        estateDict = {
                'ang-mo-kio': 'Mature Estate',
                'bedok': 'Mature Estate',
                'bishan': 'Mature Estate',
                 'bukit-batok': 'Non-Mature Estate',
                 'bukit-merah': 'Mature Estate',
                 'bukit-panjang': 'Non-Mature Estate',
                 'bukit-timah': 'Mature Estate',
                 'central': 'Mature Estate',
                 'choa': 'Non-Mature Estate',
                 'clementi': 'Mature Estate',
                 'geylang': 'Mature Estate',
                 'hougang': 'Non-Mature Estate',
                 'jurong-east': 'Non-Mature Estate',
                 'jurong-west': 'Non-Mature Estate',
                 'kallang': 'Mature Estate',
                 'marine-parade': 'Mature Estate',
                 'pasir-ris': 'Mature Estate',
                 'punggol': 'Non-Mature Estate',
                 'queenstown': 'Mature Estate',
                 'sembawang': 'Non-Mature Estate',
                 'sengkang': 'Non-Mature Estate',
                 'serangoon': 'Mature Estate',
                 'tampines': 'Mature Estate',
                 'toa-payoh': 'Mature Estate',
                 'woodlands': 'Non-Mature Estate',
                 'yishun': 'Non-Mature Estate'
                 }
        # Info from https://stackedhomes.com/hdb-estates.html
    
        # Checks eligibility
        # Checks if estateType is Non-Mature in estateTypeDict
        # Assumes estateType is in estateTypeDict
        if self.firstTimeOwner == 0:
            return 0         
        if estateDict[self.propertyLocation] == 'Mature Estate':
            return 0
        if self.monthlyIncome > 8500:
            return 0
        if self.housingType == 'EC':
            return 0
        
        SHGDict = {
                1500: 40000,
                2000: 40000,
                2500: 40000,
                3000: 40000,
                3500: 40000,
                4000: 40000,
                4500: 40000,
                5000: 40000,
                5500: 35000,
                6000: 30000,
                6500: 25000,
                7000: 20000,
                7500: 15000,
                8000: 10000,
                8500: 5000
                }
        # Info from https://dollarsandsense.sg/complete-guide-to-hdb-housing-grants-in-singapore-for-different-types-of-flats/
        
        for incomeCeiling in SHGDict:
            if self.monthlyIncome <= incomeCeiling:
                SHGValue = SHGDict[incomeCeiling]
                break
        return SHGValue
    
    def CPFHGAmount(self):
        # Returns CPF housing grant values, if any
        
        # Checks eligibility
        if self.firstTimeOwner == 0:
            return 0
        if self.monthlyIncome > 12000:
            return 0
        
        if self.housingType == '4room':
            return 50000
        if self.housingType == '5room':
            return 40000
        if self.housingType == 'EC':
            if self.monthlyIncome <= 10000:
                return 30000
            if self.monthlyIncome <= 11000:
                return 20000
            else:
                return 10000
            
    def PHGAmount(self):
        # Checks eligibility
        if self.firstTimeOwner == 0:
            return 0    
        if self.housingType == 'EC':
            return 0
        
        return 20000 if self.proximityFromParents == 1 else 0

        
    def totalGrant(self):
        # Returns total value of grants
        totalGrantValue = self.AHGAmount() + self.SHGAmount() + self.CPFHGAmount() + self.PHGAmount()
        return totalGrantValue
    
    # To determine the loan duration
    def durationCal(self):  
        # http://www.moneysense.gov.sg/life-events/buying-a-home.aspx
        # Take generically a 25-year housing loan
        # Housing loan cannot mature after one's retirement age (in SG it is defined as 65)
        retireAge = 65 
        if retireAge - self.age > 25:
            nPeriod = 25
        else:
            nPeriod = retireAge - self.age
        return nPeriod

    #Calculate monthly payment of loan
    def pmtCal(self):
        #assume 10 - 30% of disposable income can be used to finance loan 
        financePortion = 0.30 
        monthlyPayment = financePortion * (self.monthlyIncome - self.expenses)
        return monthlyPayment
        
    #To determine how much loan we can issue
    def loanCal(self):
        nPeriod12 = self.durationCal() * 12 #loan duration in months
        return abs(np.pv(0.02/12, nPeriod12, self.pmtCal(), fv=0, when = 'end'))    

    def priceCeiling(self):
        #http://www.moneysense.gov.sg/life-events/buying-a-home.aspx
        #Limit-to-value is 75% for less than 25 year loan tenure
        if self.existingLoan == 0:
            return min(self.availDownPay/0.25, self.availDownPay + self.loanCal())
        if self.existingLoan == 1:
            return min(self.availDownPay/0.55, self.availDownPay + self.loanCal())
        if self.existingLoan >= 2:
            return min(self.availDownPay/0.65, self.availDownPay + self.loanCal())




def main():
    while 1:
        try:
            age = int(input("Please define your age, as of this year: ")) #Loan Duration, Risk
        except ValueError:
            print("Please enter a valid age!")
        if age <= 0:
            print("Age cannot be zero or negative!")
        else:
            break
    
        
    gender = 'M'
    
    while 1:
        try:
            monthlyIncome = int(input("Please enter your estimated monthly income, rounded to the nearest dollar: ")) #Loan Calculation
        except ValueError:
            print("Please enter a valid value!")
        if monthlyIncome < 0:
            print("Monthly income cannot be negative!")
        else:
            break

    while 1:
        try:
            expenses = int(input("Please enter your estimated monthly expenses, rounded to the nearest dollar: ")) #Loan Calculation
        except ValueError:
            print("Please enter a valid value!")
        if expenses < 0:
            print("Expenses cannot be negative!")
        else:
            break

    personalSavings = 0


    while 1:
        try:
            availDownPay = int(input("Please enter the amount of funds you have available to downpay, rounded to the nearest dollar: ")) #downpayment calculation
        except ValueError:
            print("Please enter a valid value!")    
        if availDownPay < 0:
            print("Available downpayment cannot be negative!")
        else:
            break
        
    while 1:
        try:
            existingLoan = int(input("Please enter the number of existing housing loans you have: ")) #downpayment calculation
        except ValueError:
            print("Please enter a valid value!")
        if existingLoan < 0:
            print("Existing loan cannot be negative!")
        else:
            break             
    
    propertyLocation = 'tampines' #filter
 
    buyer = Buyer(age, gender, monthlyIncome, expenses, personalSavings, availDownPay, existingLoan, propertyLocation)
    
    # Estimates maximum price of house to display
    maxAffordability = buyer.priceCeiling()
    maxAffordability += 20000
    
    
    print('The amount you are estimated to be able to afford is:' + "{0:,}".format(maxAffordability))
        
    # Show housing list
    priceFilterHousingList = priceFilter(maxAffordability)
    shownHousingList = locationFilter(priceFilterHousingList, buyer.propertyLocation)
    print('Name         ', 'Price    ', ' Type    ', '  Location    ')
    for row in shownHousingList:
        print(str(row[0])+' '*4, str(row[1])+' '*(10-len(str(row[1]))), str(row[2])+' '*(10-len(row[2])), str(row[3]))
    
    #-----------------------------------------------------------------------------------------
    # Execute if user wants to sort by Property Type or Price, Ascending or Descending
    
    sortBy = input("Sort by:")
    sortOrder = input("Ascending or Descending:")
    
    newHousingList = sortingAttribute(shownHousingList, sortBy, sortOrder)
    shownHousingList = newHousingList
    print('Name         ', 'Price    ', ' Type    ', '  Location    ')
    for row in shownHousingList:
        print(str(row[0])+' '*4, str(row[1])+' '*(10-len(str(row[1]))), str(row[2])+' '*(10-len(row[2])), str(row[3]))
    
    #------------------------------------------------------------------------------------------
    # Execute below after user clicks on property
    
    # Suppose that X is house chosen from shownHousingList
    X = shownHousingList[1]
    buyer.setHousingType(X[2])
    
    dummyFirstTimeOwner = input("Are you a first time homeowner? Y/N")
    if dummyFirstTimeOwner == 'N':
        buyer.notFirstTimeOwner()
        
    dummyProximityFromParents = input("Are staying within 4km from your parents? Y/N")
    if dummyProximityFromParents == 'N':
        buyer.notNearParents()
    
    dummyworked12Months = input("At least 1 of the applicants must have worked continuously for 12 months prior to the flat application, and still be employed at the point of flat application. Is this true for you? Y/N")
    if dummyworked12Months == 'N':
        buyer.notWorked12Months()
        
    totalGrant = buyer.totalGrant()
    print('You are qualified for a total grant amount of: $' + str(totalGrant) + '\n')
    print('CPF Housing Grant amount: $' + str(buyer.CPFHGAmount()))
    print('Additional CPF Housing Grant amount: $' + str(buyer.AHGAmount()))
    print('Special CFP Housing Grant amount: $' + str(buyer.SHGAmount()))
    print('Proximity Housing Grant amount: $' + str(buyer.PHGAmount()) + '\n')
    
    requiredPayment = 0
    if X[1]/4 < buyer.availDownPay:
        requiredPayment = X[1]/4
    else:
        requiredPayment = X[1] - totalGrant - buyer.loanCal()
    if requiredPayment < 0:
        requiredPayment = 0
    print("Assuming that you take the maximum 25 year loan amount, you will have to pay $ " + str(requiredPayment))    
    print("This means drawing down " + str(round(requiredPayment/buyer.availDownPay,2)*100) + "% of your maximum available downpayment.")
    
def priceFilter(maxAffordability):
    # Compare with database of houses
    import HouseDatabaseGenerator
    houseDatabase = HouseDatabaseGenerator.generateHouseDB()
    # Sort by price
    houseDatabaseByPrice = sorted(houseDatabase, key=lambda x: x[1])
    
    for row in range(len(houseDatabaseByPrice)):
        if (maxAffordability < houseDatabaseByPrice[row][1]):
            return houseDatabaseByPrice[:row]
            break
        else:
            continue
    return houseDatabaseByPrice

def locationFilter(priceFilterHousingList, propertyLocation):
    displayList = []
    for x in priceFilterHousingList:
        if x[3] == propertyLocation:
            displayList.append(x)       
    return displayList

def sortingAttribute(shownHousingList, sortBy, sortOrder):
    sortOrderBool = 1
    if sortOrder == 'Ascending':
        sortOrderBool = 0

	# Sort shownHousingList list
    if sortBy == "Price":
        return sorted(shownHousingList, key=lambda x:x[1], reverse = sortOrderBool)
    elif sortBy == "Property Type":
        return sorted(shownHousingList, key=lambda x:x[2], reverse = sortOrderBool)

if __name__ == '__main__':
    main()