import csv 
#Scan a badge, will retrieve the badge ID from the dict and the number, and place in a new dict which will be saved into the final csv to be copy pasted into the form
additionToDayPassFile = {}
dayPassDict = {}
dayPassFinalDict = {}
badgeQuantitiesArray = []
counter = 0
index  = 0
#Opens the dayPassFile which stores all our daypasses
with open('DayPasses/dayPassFile.csv', mode = "r") as file:
    dayPassFile = csv.reader(file)

    for lines in dayPassFile:
        dayPassDict[lines[0]] = lines[1]
        # print(lines)


# while True:
#     print("Enter the amount quantities of badges to be scanned (examples 4 or 10),type done when finished:")
#     badgeQuantities = input()   
#     if badgeQuantities == "done":
#         break
#     else:
#         #TODO Make sure this is a int not a string or anything else.
#         badgeQuantitiesArray.append(int(badgeQuantities))
#         print(badgeQuantitiesArray)

        
# Scans badges and pulls the data from the original dict into the final dict
while True:
    print("Scan a Badge:")
    badgeId = input()
    if badgeId == "done":
        break
    elif badgeId in dayPassDict:
        dayPassFinalDict[badgeId] = dayPassDict[badgeId]
        print("Current Badges: ")
        print(dayPassFinalDict)
        print("Badges Scanned: " + str(len(dayPassFinalDict)))
    else:
        print("Not currently in Dict, Please enter the ID number:")
        badgeNumber = input()
        additionToDayPassFile[badgeId] = badgeNumber
        dayPassFinalDict[badgeId] = badgeNumber
        print("Current Badges: ")
        print(dayPassFinalDict)
        print("Badges Scanned: " + str(len(dayPassFinalDict)))

#TODO figure out how to add a new line every badgeQuanityArray[i]
with open('DayPasses\dayPassFileFinal.csv', mode = "w", newline = '') as file:
    writer = csv.writer(file, delimiter='\t')
    # writing data rows 
    for key, value in dayPassFinalDict.items():
        writer.writerow([value, key])

with open('DayPasses/dayPassFile.csv', mode = 'a', newline = '') as file:
    writer = csv.writer(file, delimiter='\t')

    for key,value in additionToDayPassFile.items():
        writer.writerow([value,key])
