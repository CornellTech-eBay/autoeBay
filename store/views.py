from django.shortcuts import render
from django.http import HttpResponse

import pickle


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def load_obj(name):
    with open('./trendsData/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def getNestedList(itemDictList):
    keywordsList = itemDictList["keywordsList"]
    itemList = []
    n = 0
    while len(itemList) < 20:
        for keyword in keywordsList:
            if (len(itemDictList[keyword]) > n):
                itemList.append(itemDictList[keyword][n])
                if len(itemList) == 20: break

    nitemList = []
    for i in range(4):
        nitemList.append(itemList[i*5:(i+1)*5])
    return nitemList

def index(request):
    itemDictList = load_obj('parsedData')
    itemList = getNestedList(itemDictList)

    context = {'itemList': itemList}
    return render(request, 'store/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")
