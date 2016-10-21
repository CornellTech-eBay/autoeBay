import csv

def loadeBay(name):
    eBayItemList = []
    with open('./trendsData/' + name + '.csv', mode='r') as infile:
        reader = csv.reader(infile)
        keywordsList = next(reader)
        for row in reader:
            tdict = {}
            for i in range(len(keywordsList)):
                tdict[keywordsList[i]] = row[i]
            eBayItemList.append(tdict)
    return eBayItemList


eBayItemList = loadeBay('ebayHomePage')
print(eBayItemList)
print(len(eBayItemList))
