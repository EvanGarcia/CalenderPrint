'''
Evan Garcia
Professor Tindall
CSC 4800
January 18, 2017

This program outputs the calender for a given four digit year (ex: 1998) to a text file.

'''


from math import floor
from collections import OrderedDict
 

def createFile(year):
    '''
    This Function takes in the year entered by the user, and creates a text file for that year's calender. It then returns the file variable calenderOutputFile
    for later use.
    '''

    calendarOutputFile = open("calendar" + year + ".txt", "w")

    return calendarOutputFile

def dayOfWeekMonthStarts(year):

    '''
    Takes in the year entered by the user, and calculates what day of the week the year starts. It returns this value as dayOfWeek to main.
    '''

    dayOfWeek = ((year + floor(((year -1 )/4)) - floor(((year - 1)/100)) + floor(((year - 1)/400))) % 7)
    
    return dayOfWeek

def isLeapYear(year):

    '''
    Takes is the year entered by the user, and determines if the year is a leap year or not. It returns either true or false to main.
    '''

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
          return True
    else:
        return False


def printCalendar(year, dayOfWeek, MonthDict, DayDict, outputFile):

    '''
    This function takes in the year entered by the user (year), the day of the week the year starts (dayOfWeek), a dictionary of month names:amount of days (MonthDict),
    a dictionary of day names: day value (DayDict), and the file to write to (outputFile). The function then writes and formats the calender to teh outputFile.
    '''
    
    startDay = int(dayOfWeek)
   
    currentDay = startDay


    for key, value in MonthDict.items():
        startDay = currentDay
        if(startDay == 7):
            startDay = 0
        tempVal = value
        outputFile.write("\n\n\n\t   " + key + " " + year + "   \n")
        for k, v in DayDict.items():
            outputFile.write(" " + k + " ")
        outputFile.write("\n")
        if(currentDay == startDay):
            outputFile.write("     " * currentDay) 
        for i in range(1, tempVal + 1):
            if(currentDay == 7):
                currentDay = 0
            outputFile.write("  {:2} ".format(i))  
            currentDay = currentDay + 1
            if(currentDay % 7 == 0):
                outputFile.write("\n")          
        startDay = startDay + 1
    outputFile.close()


def main():

    #Asks the user to enter a 4 digit year
    print("Please enter a 4-digit year value: ")
    yearSelectedString = input()
    yearSelectedInt = int(yearSelectedString)
    
    #If the value is not a 4 digit year, reask user for input 
    while(yearSelectedInt < 1000 or yearSelectedInt > 9999):
       print("Not a valid year!\n")
       print("Please enter a 4-digit year value: ")
       yearSelectedString = input()
       yearSelectedInt = int(yearSelectedString)

    #Create the file
    calendarOutputFile = createFile(yearSelectedString)
    
    #Create dictionaries for the days of week and months of year
    DaysDict = OrderedDict([("Sun", 0), ("Mon", 1), ("Tue", 2), ("Wed", 3), ("Thu", 4), ("Fri", 5), ("Sat", 6)])

    MonthsDict = OrderedDict([("January" , 31), ("February" , 28), ("March" , 31), ("April" , 30), ("May" , 31), ("June" , 30), ("July" , 31),
                              ("August" , 31), ("September" , 30) , ("October" , 31), ("November" , 30), ("December" , 31)])


    #If the year is a leap year, then change February to have 29 days
    if(isLeapYear(yearSelectedInt) == True):
        MonthsDict["February"] = 29

    #Calculate the day of week the year starts
    monthStartDay = dayOfWeekMonthStarts(yearSelectedInt)

    #Print the calender to the file
    printCalendar(yearSelectedString, monthStartDay, MonthsDict, DaysDict, calendarOutputFile)
    






if __name__ == "__main__":
    main()