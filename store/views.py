from django.shortcuts import render
from django.http import HttpResponse
from random import shuffle

import pickle
import csv


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def save_obj(obj, name):
    with codecs.open('trendsData/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)

def load_obj(name):
    with open('./trendsData/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def getItemList(itemDictList):
    keywordsList = itemDictList["keywordsList"]
    itemList = []
    n = 0
    while len(itemList) < 20:
        tlen = len(itemList)
        for keyword in keywordsList:
            if (len(itemDictList[keyword]) > n):
                itemList.append(itemDictList[keyword][n])
                if len(itemList) == 20: break
        if (tlen == len(itemList)): break
        n = n + 1
    return itemList


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


def index(request):
    itemDictList = load_obj('parsedData')
    itemList = getItemList(itemDictList)

    eBayItemList = loadeBay('ebayHomePage')

    # itemList = itemList[0:min(10, len(itemList))] + eBayItemList

    # shuffle(itemList)

    print(len(itemList))

    nitemList = []
    for i in range(4):
        nitemList.append(itemList[i*5:(i+1)*5])
    itemList = nitemList

    context = {'itemList': itemList}
    return render(request, 'store/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")
