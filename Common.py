import re
from Decision import Decision
from Param import Param


def listAttributesAndTheirNumbers(self):
    lines = splitIntoLines(self)
    myArray = []
    for line in lines:
        myArray.append(line.split(" "))
    return myArray


def printFile(self):
    f = open(self)
    print(f.read())


def splitIntoLines(self):
    return re.split(r'\n', self)


def delLastColumnAndRow(self):
    for i in range(len(self)):
        print(len(self[i]))
        print(self[i][0])
        del self[i][len(self[i]) - 1]
    del self[len(self) - 1]
    return self


def switchColumnsToRows(self):
    result = []
    for x in range(len(self[0])):
        row = []
        for i in range(len(self)):
            a = len(self)
            row.append(self[i][x])
        result.append(row)
    return result


def getDecisions(array):
    result = []
    for i in range(len(array)):
        if not array[i][len(array[i]) - 1] in result:
            result.append(array[i][len(array[i]) - 1])
    return result


def getIndexOfDecision(array):
    decisions = getDecisions(array)
    result = []
    for x in decisions:
        decisionObject = Decision()
        decisionObject.setDecision(x)
        list = []
        for i in range(len(array)):
            if array[i][len(array[i]) - 1] == x:
                list.append(i)
        decisionObject.setIndexList(list)
        result.append(decisionObject)
    return result


def countParam(array, indexOfDecisions, trnArray):
    i = 0
    listOfParam = []
    for xX in array:
        i += 1
        param = Param()
        for decision in indexOfDecisions:
            param = Param()
            param.setTestObject("x" + str(i))
            param.setCObjet(decision.getDecision())
            j = 0
            listOfParamCounter = []
            whichElem=0
            for elemOfX in xX:
                counter = 0
                for k in decision.getIndexList():
                    if elemOfX == trnArray[k][whichElem]:
                        counter += 1
                whichElem+=1
                listOfParamCounter.append(counter/len(decision.getIndexList()))
            paramResult = (1/2)*sum(listOfParamCounter)
            param.setParam(paramResult)
            listOfParam.append(param)
    return listOfParam

