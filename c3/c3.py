import Common
import random

class TrainAndTest():
    def main(self):
        print("T&T")
        fDec = open("result/dec_bayesT&T.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        randomSystemIndexList = TrainAndTest.generateTRNandTSTIndexList(lines, 0.5)
        randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
        randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
        countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
        classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem), fDec)
        globalAccuracy = Common.getGlobalAccuracy(classified)
        allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
        print("Global accuracy = " + str(globalAccuracy))
        print("Balanced accuracy = " + str(Common.getBalancedAccuracy(allClasses, classified)))
        fAcc = open("result/acc_bayesT&T.txt", "w+")
        fAcc.write(f"Global accuracy = " + str(globalAccuracy) + "\nBalancedAccuracy = " + str(
            Common.getBalancedAccuracy(allClasses, classified)))
        print("abc")

    # Returns 2d array
    # Row #1 - trn array
    # Row #2 - tst array
    #T&T
    def generateTRNandTSTIndexList(array, ratio):
        arrayLen = len(array)
        result = []
        trnArray = []
        tstArray = []
        for i in range(int(arrayLen*ratio)):
            added = False
            while not added:
                k = random.randint(0, arrayLen-1)
                if(not trnArray.__contains__(k)):
                    trnArray.append(k)
                    added = True

        result.append(trnArray)

        for j in range(arrayLen):
            if not trnArray.__contains__(j):
                tstArray.append(j)
        result.append(tstArray)
        return result

    def fromIndexToList(indexList, list):
        result = []
        for i in indexList:
            result.append(list[i])
        return result

class BootStrapMethod():
    def main(self):
        print("Bootstrap")
        fDec = open("result/dec_bayesBootstrap.txt", "w+")
        lines = Common.listAttributesAndTheirNumbers(open("australian.txt").read())
        randomSystemIndexList = BootStrapMethod.generateTRNandTSTIndexList(lines, 100)
        randomTrnSystem = Common.fromIndexToList(randomSystemIndexList[0], lines)
        randomTstSystem = Common.fromIndexToList(randomSystemIndexList[1], lines)
        countedParams = Common.countParam(randomTstSystem, randomTrnSystem)
        classified = Common.numOfCorrectlyClassified(countedParams, Common.getListOfDecisionsTST(randomTstSystem), fDec)
        globalAccuracy = Common.getGlobalAccuracy(classified)
        allClasses = Common.unique(Common.getListOfDecisionsTST(lines))
        print("Global accuracy = " + str(globalAccuracy))
        print("Balanced accuracy = " + str(Common.getBalancedAccuracy(allClasses, classified)))
        fAcc = open("result/acc_bayesBootstrap.txt", "w+")
        fAcc.write(f"Global accuracy = " + str(globalAccuracy) + "\nBalancedAccuracy = " + str(
            Common.getBalancedAccuracy(allClasses, classified)))
        print("abc")

    # Returns 2d array
    # Row #1 - trn array
    # Row #2 - tst array
    # T&T
    def generateTRNandTSTIndexList(array, numOfElements):
        arrayLen = len(array)
        result = []
        trnArray = []
        tstArray = []
        for i in range(numOfElements):
            k = random.randint(0, arrayLen - 1)
            if (not trnArray.__contains__(k)):
                trnArray.append(k)

        result.append(trnArray)

        for j in range(arrayLen):
            if not trnArray.__contains__(j):
                tstArray.append(j)
        result.append(tstArray)
        return result



if __name__ == "__main__":
    TrainAndTest.main("args")
    BootStrapMethod.main("args")

